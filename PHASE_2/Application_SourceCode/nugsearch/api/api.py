from flask import Flask, abort, request
from apiKey import key
import requests

app = Flask(__name__)

@app.route('/currentLocation')
def currentLocation():
    if 'lon' not in request.args or 'lat' not in request.args:
        abort(400)
    print ("Location Request :)")
    lat = request.args['lat']
    lon = request.args['lon']
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
    return {
        "startDate": startDate,
        "endDate": endDate,
        "keywords": keywords,
        "location": location
    }

@app.route('/getAlerts')
def getAlerts():
    return {
        # Can't have spaces in these names
        "alerts": ["Covid-19", "BlackDeath", "Rabies"]
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
    return {}

@app.route('/')
def index():
    return{
        "possible_endpoints": [
            "currentLocation",
            "search",
            "getAlert",
            "getAlertDescription"
        ]
    }