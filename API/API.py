import flask
from flask import request, jsonify
import mysql.connector
import simplejson as json
from datetime import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/', methods=['GET'])
def home():
    return "<h1>SENG3011 McNuggets API</h1><p>API for ProMedMail.org</p>"

@app.route('/search', methods=['GET'])
def filter_search():
    query_parameters = request.args
    start_date = query_parameters.get('start_date')
    end_date = query_parameters.get('end_date')
    key_terms = query_parameters.get('key_terms')
    location = query_parameters.get('location')

    query = ""
    to_filter = []

    if start_date:
        query += ' start_date=? AND'
        to_filter.append(start_date)
    if end_date:
        query += ' end_date=? AND'
        to_filter.append(end_date)
    if key_terms:
        query += ' key_terms=? AND'
        to_filter.append(key_terms)
    if location:
        query += ' location=? AND'
        to_filter.append(location)
    if not (start_date or end_date or location):
        return page_not_found(404)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="newrootpassword",
        auth_plugin='mysql_native_password',
        database="promedmail"
    )

    start = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S')
    end = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S')
    mycursor = mydb.cursor()
    sql = "select * from articles where pubDate >= %s and pubDate <= %s;"
    sql2 = "select * from locations;"
    data = (start, end)
    mycursor.execute(sql, data)
    record = mycursor.fetchall()


    # Connect to DB
    # Query Articles DB for publication date
    # If articles reports do not include key_terms or location, remove from dict

    results = record
    return jsonify(results)

app.run()