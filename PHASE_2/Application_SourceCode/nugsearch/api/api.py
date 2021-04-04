from flask import Flask

app = Flask(__name__)

@app.route('/currentLocation')
def currentLocation():
    print ("Sydney")
    return {
        "location": "Sydney"
    }

@app.route('/search')
def search():
    return {
        "result": "Test result"
    }

@app.route('/getAlert')
def getAlert():
    return {}

@app.route('/getAlertDescription')
def getAlertDescription():
    return {}