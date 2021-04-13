from flask import Flask, request

app = Flask(__name__)

@app.route('/currentLocation')
def currentLocation():
    print ("Sydney")
    return {
        "location": "Sydney"
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