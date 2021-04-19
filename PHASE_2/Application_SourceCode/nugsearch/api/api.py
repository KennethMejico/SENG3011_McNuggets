from flask import Flask, abort, request
from apiKey import key
from mapData import getCaseLocations, getRegions
import requests

app = Flask(__name__)

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
        "alerts": ["Covid-19", "BlackDeath"]
    }

@app.route('/getAlertDescription')
def getAlertDescription():
    if "Covid-19" == request.args.get("name"):
        return {
            "title": "Covid-19 Outbreak",
            "text": "There were 17 cases of COVID-19 in Sydney on 10/04/2021. In the past, this amount of cases has lead to a lockdown in your area. Be prepared for another to happen again. COVID-19 has caused a lockdown in your area THREE times before. COVID-19 has caused lockdowns to happen way too many times in total. The last COVID-19 lockdown happened after 15 cases were reported in a day. See government alerts for your area: https://www.nsw.gov.au/"
        }
    elif "BlackDeath" == request.args.get("name"):
        return {
            "title": "Black Death Resurgeance",
            "text": "Somehow, the black death has returned"
        }
    return {
        "title": "Bad Alert string",
        "text": "Bad Alert string"
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

@app.route('/')
def index():
    return{
        "possible_endpoints": [
            "currentLocation",
            "search",
            "getAlert",
            "getMap",
            "getAlertDescription"
        ]
    }