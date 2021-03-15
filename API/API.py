import flask
from flask import request, jsonify
import mysql.connector
import simplejson as json
from datetime import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_SORT_KEYS'] = False

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

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/', methods=['GET'])
def home():
    return "<h1>SENG3011 McNuggets API</h1><p>API for ProMedMail.org</p>"

@app.route('/search', methods=['GET'])
def filter_search():
    # Retrieve parameters
    query_parameters = request.args
    start_date = query_parameters.get('start_date')
    end_date = query_parameters.get('end_date')
    key_terms = query_parameters.get('key_terms')
    location = query_parameters.get('location')

    if not (start_date or end_date):
        return page_not_found(404)

    # Connect to MySQL Database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="newrootpassword",
        auth_plugin='mysql_native_password',
        database="promedmail"
    )

    # Convert start_date and end_date to datetime
    start = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S')
    end = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S')

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
    """
    
    # Convert start and date time to datetime datatype
    start = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S')
    end = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S')

    # Case 1: Only period of interest input
    if (start_date and end_date and not key_terms and not location):
        sql = sql + "where pubDate >= %s and pubDate <= %s;"
        data = (start, end)
        result = retrieve_data(mycursor, sql, data)
    # Case 2: Only key terms --
    # Case 3: Only locations --
    # Case 4: Period of interest and locations
    elif (start_date and end_date and not key_terms and location):
        sql1 = sql + "where pubDate >= %s and pubDate <= %s and locationName = %s"
        data = (start, end, location)
        result = retrieve_data(mycursor, sql1, data)
    # Case 5: Period of interest and key_terms
    elif (start_date and end_date and key_terms and not location):
        sql1 = sql + "where pubDate >= %s and pubDate <= %s and (disease LIKE %s or syndrome LIKE %s)"
        key_terms = "%" + key_terms + "%"
        data = (start, end, key_terms, key_terms)
        result = retrieve_data(mycursor, sql1, data)
    # Case 6: Key terms and locations --
    # Case 7: All Three
    elif (start_date and end_date and key_terms and location):
        sql1 = sql + "where pubDate >= %s and pubDate <= %s and locationName = %s and (disease LIKE %s or syndrome LIKE %s)"
        key_terms = "%" + key_terms + "%"
        data = (start, end, location, key_terms, key_terms)
        result = retrieve_data(mycursor, sql1, data)

    # Return list of articles
    return jsonify(result)

# Possible Endpoints
# @app.route('/count', methods=['GET'])
# @app.route('/getDatabase', methods=['GET'])
# @app.route('/images', methods=['GET'])
# @app.route('/list/diseases', methods=['GET'])
# @app.route('/list/syndromes', methods=['GET'])
app.run()