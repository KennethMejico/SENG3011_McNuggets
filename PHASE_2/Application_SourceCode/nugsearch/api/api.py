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
    location = ""
    dateStart = ""
    dateEnd = ""
    kwords = ""
    reqURL = ""
    return {
        "result": "Test result"
    }

@app.route('/getAlert')
def getAlert():
    return {}

@app.route('/getAlertDescription')
def getAlertDescription():
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