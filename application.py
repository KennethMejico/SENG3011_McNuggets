import flask
from flask import request, jsonify
import mysql.connector
import simplejson as json
from datetime import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_SORT_KEYS'] = False

# Returns pointer to db connector
def connect_to_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="newrootpassword",
        auth_plugin='mysql_native_password',
        database="promedmail"
    )
    return mydb

# Retrieves data from MySQL server and returns a list of articles
def retrieve_data(mycursor, sql, data):
    mycursor.execute(sql, data)
    results = mycursor.fetchall()
    article_list = []
    for article in results:
        article_list.append(convert(article))
    return article_list

# Converts SQL data to python dict/list form
def convert(lst):
    reports_list = []
    # This needs to be updated in future when multiple reports are assigned to a single article
    report_dict = {'event_date':lst[4], 'locations':lst[5], 'diseases': lst[6], 'syndromes': lst[7]}
    reports_list.append(report_dict)
    article_dict = {'url':lst[0], 'date_of_publication':lst[1], 'headline':lst[2], 'main_text':lst[3], 'reports': reports_list}
    return article_dict

def noneOrEmpty(str):
    return (str is None) or (not str)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.errorhandler(400)
def dates_not_given(e):
    return "<h1>400</h1><p>Please input a start and end date.</p>", 400

@app.route('/', methods=['GET'])
def home():
    return """<!DOCTYPE html>
<html>
<title>McNuggets API</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<style>
body,h1 {font-family: "Raleway", sans-serif}
body, html {height: 100%}
.bgimg {
  min-height: 100%;
  background-position: center;
  background-size: cover;
}
</style>
<body>
<div class="bgimg w3-display-container w3-animate-opacity w3-text-black">
  <div class="w3-display-topleft w3-padding-large w3-xlarge">
    SENG3011
  </div>
  <div class="w3-display-middle">
    <h1 class="w3-jumbo w3-animate-top">McNuggets API</h1>
    <hr class="w3-border-grey" style="margin:auto;width:40%">
    <p class="w3-large w3-center">Extraction from ProMedMail.org</p>
  </div>
</div>
</body>
</html>"""

@app.route('/search', methods=['GET'])
def filter_search():
    # Retrieve parameters
    query_parameters = request.args
    start_date = query_parameters.get('start_date')
    end_date = query_parameters.get('end_date')
    key_terms = query_parameters.get('key_terms')
    location = query_parameters.get('location')

    if noneOrEmpty(start_date) or noneOrEmpty(end_date):
        return dates_not_given(400)

    mydb = connect_to_db()

    # Execute query to gather articles which satisfy data constraint
    mycursor = mydb.cursor()

    # Base SQL Query
    sql = """
        select
            a.linkToArticle,
            a.pubDate,
            a.articleName,
            a.mainText,
            r.eventDate,
            l.locationName,
            r.disease,
            r.syndrome
        from
            articles a
        left join
            reports r on r.articleID = a.articleID
        left join
            locations l on r.locationID = l.locationID
        where a.pubDate >= %s and a.pubDate <= %s
    """
    
    # Convert start and date time to datetime datatype
    start = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S')
    end = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S')

    data = (start, end)

    if not noneOrEmpty(location):
        sql = sql + " and l.locationName = %s"
        data = data + (location,)

    if not noneOrEmpty(key_terms):
        sql = sql + " and (r.disease LIKE %s or r.syndrome LIKE %s)"
        formatted_key_terms = "%" + key_terms + "%"
        data = data + (formatted_key_terms, formatted_key_terms,)
    
    result = retrieve_data(mycursor, sql, data)

    # Return list of articles
    return jsonify(result)

@app.route('/getDatabase', methods=['GET'])
def get_all_reports():
    mydb = connect_to_db()

    # Execute query to gather articles which satisfy data constraint
    mycursor = mydb.cursor()
    sql = """
        select
            a.linkToArticle,
            a.pubDate,
            a.articleName,
            a.mainText,
            r.eventDate,
            l.locationName,
            r.disease,
            r.syndrome
        from
            articles a
        left join
            reports r on r.articleID = a.articleID
        left join
            locations l on r.locationID = l.locationID
    """
    mycursor.execute(sql)
    results = mycursor.fetchall()
    article_list = []
    for article in results:
        article_list.append(convert(article))
    result = article_list

    # Return list of articles
    return jsonify(result)

#@app.route('/count', methods=['GET'])

# Possible Endpoints\
# @app.route('/images', methods=['GET'])
# @app.route('/list/diseases', methods=['GET'])
# @app.route('/list/syndromes', methods=['GET'])
app.run()
application = app
