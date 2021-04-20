from flask import Flask, abort, request
from apiKey import key
from mapData import getCaseLocations, getRegions
import requests
import json
from datetime import date
from flask_mail import Mail, Message
import os

app = Flask(__name__)
mail = Mail(app)

emailAddress = "sengMcNuggets@gmail.com"
emailPassword = os.environ['EMAIL_PASSWORD']

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = emailAddress
app.config['MAIL_PASSWORD'] = emailPassword
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/currentLocation')
def currentLocation():
    if 'lon' not in request.args or 'lat' not in request.args:
        abort(400)
    print ("Location Request :)")
    lat = request.args['lat']
    lon = request.args['lon']
    if lat is None or lon is None:
        abort(400)
    reqURL = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(lat) + "," + str(lon) + "&key=" + key + "&location_type=APPROXIMATE"
    response = requests.get(reqURL)
    resJSON = response.json()
    location = resJSON['results'][0]['formatted_address'] # We use the first approximation, it's generally the city/locality
    return {
        "location": str(location)
    }

@app.route('/search')
def search():
    startDate = request.args.get("startDate")
    endDate = request.args.get("endDate")
    keywords = request.args.get("keywords")
    location = request.args.get("location")

    # url = f"http://52.15.58.197:8000/v1/articles?start={startDate}&end={endDate}&keywords={keywords}&location={location}"

    formattedStart = startDate[:-5]
    formattedEnd = endDate[:-5]

    # url = f"https://4k6yve9rsa.execute-api.ap-southeast-2.amazonaws.com/default/mcnuggets/search?start_date={formattedStart}&end_date={formattedEnd}&key_terms={keywords}&location={location}"

    url = f"https://api.bugfree.team/articles?start_date={formattedStart}&end_date={formattedEnd}&key_terms={keywords}&locations={location}"

    response = requests.get(url)
    print(response.json())
    return response.json()

@app.route('/getAlerts')
def getAlerts():
    return {
        # Can't have spaces in these names
        "alerts": ['nsw', 'qld', 'vic', 'wa', 'sa', 'tas', 'act', 'nt']
    }

@app.route('/getMap')
def getMap():
    if 'date' not in request.args or 'location' not in request.args:
        abort(400)
    print ("Map Data Request")
    date = request.args['date']
    unparsed_location = request.args['location']
    print("Date: "+date+", location: "+unparsed_location)
    if date is None or unparsed_location is None:
        abort(400)
    
    reqURL = "https://maps.googleapis.com/maps/api/geocode/json?address=" + unparsed_location + "&key=" + key
    response = requests.get(reqURL)
    resJSON = response.json()
    if resJSON["status"] != 'OK':
        print("Error Occured in google geocoding: " + resJSON.status)
        abort(400)
    location = resJSON["results"][0]["geometry"]["location"]
    # Location is a dict with two keys, lat and lng

    regions = getRegions(date, location)
    caseLocations = getCaseLocations(date, location)
    
    return {
        "center": location,
        "regions": regions,
        "caseLocations": caseLocations
    }

@app.route('/getAlertData')
def getAlertData():
    location = request.args.get("location")

    try:
        with open("covid19Data.json", 'r') as f:
            data = json.load(f)
        return { "location": location,
                 "average": data[location]['average'],
                 "latest": data[location]['latest'],
                 "time": data[location]['curTime']
        }
    except IOError:
        pass
    return None

@app.route('/checkAlert')
def checkAlert():
    alertList = []
    try:
        with open("covid19Data.json", 'r') as f:
            data = json.load(f)
        for location in data:
            if location in ['qld', 'vic', 'nsw']:
                if float(data[location]['average']) > 1 or float(data[location]['latest']) > 5:
                    alertList.append(location)
            else:
                if float(data[location]['average']) > 0.2 or float(data[location]['latest']) > 1:
                    alertList.append(location)
    except IOError:
        pass
    return {
        "check": False,
        "alerts": alertList
    }

@app.route('/sendEmail')
def sendEmail():
    if 'email' not in request.args:
        abort(400)
    emailTarget = request.args.get('email')
    msg = Message('Welcome', sender = emailAddress, recipients = [emailTarget])
    msg.html = f"""
        <p>
        You have signed up for alerts from NugSearch
        <br><br>
        To Unsubscribe, Please go to <a href="https://localhost:3000/signupRemove?{emailTarget}"> this Link</a>
        </p>
        """
    with open("mailingList.txt", "a") as file_object:
        file_object.write(f"{emailTarget}\n")
    mail.send(msg)

    return {'ok': True}

@app.route('/')
def index():
    return{
        "possible_endpoints": [
            "currentLocation",
            "search",
            "getAlert",
            "getMap",
            "getAlertDescription",
            "checkAlert",
            "sendEmail"
        ]
    }