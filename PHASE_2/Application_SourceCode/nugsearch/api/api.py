from flask import Flask

app = Flask(__name__)

@app.route('/search')
def search():
    return {}

@app.route('/getAlert')
def getAlert():
    return {}

@app.route('/getAlertDescription')
def getAlertDescription():
    return {}