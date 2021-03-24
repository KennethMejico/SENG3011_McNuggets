import flask
from flask import request, jsonify
import mysql.connector
import simplejson as json
from datetime import datetime
import db_controller

application = app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_SORT_KEYS'] = False


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
    
    result = search(start_date, end_date, location, key_terms, db_controller.getDbConnection())

    # Return list of articles
    return jsonify(addLog(result))

def search(start_date, end_date, location, key_terms, db):
    mycursor = db.cursor()

    # Base SQL Query
    sql = """
        select
            a.LinkToArticle,
            a.PubDate,
            a.ArticleName,
            a.MainText,
            r.EventDate,
            r.ReportID
        from Articles a
        join Reports r on r.ArticleID = a.ArticleID
        where a.ArticleID = a.ArticleID
    """
    data = ()
    if not noneOrEmpty(start_date):
        # Convert start date time to datetime datatype
        start = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S')
        sql = sql + " and a.PubDate >= %s"
        data = data + (start,)

    if not noneOrEmpty(end_date):
        end = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S')
        sql = sql + " and a.PubDate <= %s"
        data = data + (end,)

    mycursor.execute(sql, data)
    results = mycursor.fetchall()

    result_list = []
    for result in results:
        report_list = []
        reportId = result[5]
        locations = getLocationsForReport(reportId, mycursor, location)
        diseases = getDiseasesForReport(reportId, mycursor, key_terms)
        syndromes = getSyndromesForReport(reportId, mycursor, key_terms)
        keywords = getKeywordsForReport(reportId, mycursor, key_terms)

        if not noneOrEmpty(location) and len(locations) == 0:
            continue
        if not noneOrEmpty(key_terms) and len(diseases) == 0 and len(syndromes) == 0 and len(keywords) == 0:
            continue

        report = {
            'event_date': result[4],
            'locations': locations,
            'diseases': diseases,
            'syndromes': syndromes
        }

        report_list.append(report)
        

        article = {
            'url': result[0],
            'date_of_publication': result[1],
            'headline': result[2],
            'main_text': result[3],
            'reports': report_list
        }

        if not noneOrEmpty(key_terms):
            split_terms = key_terms.split(',')
            for term in split_terms:
                if term.lower() in syndromes or term.lower() in diseases or term.lower() in keywords:
                    result_list.append(article)
                    break
        else:
            result_list.append(article)

    db.close()

    return result_list

@app.route('/list/reports', methods=['GET'])
def get_all_reports():
    mydb = db_controller.getDbConnection()

    result = search(None, None, None, None, mydb)
    mydb.close()

    return jsonify(addLog(result))

@app.route('/list/diseases', methods=['GET'])
def get_all_diseases():
    db = db_controller.getDbConnection()
    cursor = db.cursor()

    query = "SELECT DiseaseName from Diseases"
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()

    diseases = []
    for result in results:
        diseases.append(result[0])

    return jsonify(addLog(diseases))

@app.route('/list/syndromes', methods=['GET'])
def get_all_syndromes():
    db = db_controller.getDbConnection()
    cursor = db.cursor()

    query = "SELECT SyndromeName from Syndromes"
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()

    syndromes = []
    for result in results:
        syndromes.append(result[0])

    return jsonify(addLog(syndromes))

@app.route('/list/locations', methods=['GET'])
def get_all_locations():
    db = db_controller.getDbConnection()
    cursor = db.cursor()

    query = "SELECT LocationName from Locations"
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()

    locations = []
    for result in results:
        locations.append(result[0])

    return jsonify(addLog(locations))

# Returns a count of the number of mentions of each disease in the time range
# by default, or the number of mentions of each of the keywords if specified
@app.route('/count', methods=['GET'])
def get_count():
    # Retrieve parameters
    query_parameters = request.args
    start_date = query_parameters.get('start_date')
    end_date = query_parameters.get('end_date')
    key_terms = query_parameters.get('key_terms')

    if noneOrEmpty(start_date) or noneOrEmpty(end_date):
        return dates_not_given(400)

    db = db_controller.getDbConnection()

    mycursor = db.cursor()

    # Base SQL Query
    sql = """
        select
            r.EventDate,
            d.DiseaseName,
            count(*)
        from Diseases d
        join Report_Diseases rd on rd.DiseaseID = d.DiseaseID
        join Reports r on rd.ReportID = r.ReportID
        where r.ReportID = r.ReportID
    """
    data = ()
    if not noneOrEmpty(start_date):
        # Convert start date time to datetime datatype
        start = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S')
        sql = sql + " and r.EventDate >= %s"
        data = data + (start,)

    if not noneOrEmpty(end_date):
        end = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S')
        sql = sql + " and r.EventDate <= %s"
        data = data + (end,)
    sql = sql + "group by d.DiseaseName"

    mycursor.execute(sql, data)
    results = mycursor.fetchall()
    diseases = {}
    for disease in results:
        diseases[disease[1]] = disease[2]

    # Return list of articles
    return jsonify(addLog(diseases))

# Possible Endpoints\
# @app.route('/images', methods=['GET'])

def getLocationsForReport(reportId, cursor, location=None):
    locationQuery = """
        SELECT l.LocationName
        FROM Locations l 
        join Report_Locations rl on rl.LocationID = l.LocationID
        join Reports r on rl.ReportID = r.ReportID
        where r.ReportID = %s
    """

    locationData = (reportId,)
    if not noneOrEmpty(location):
        locationQuery = locationQuery + " and l.locationName LIKE %s"
        formatted_location = "%" + location + "%"
        locationData = locationData + (formatted_location,)
    
    cursor.execute(locationQuery, locationData)
    results = cursor.fetchall()

    locations = []
    for location in results:
        locations.append(location[0])

    return locations

def getDiseasesForReport(reportId, cursor, key_terms=None):
    query = """
        SELECT d.DiseaseName
        FROM Diseases d 
        join Report_Diseases rd on rd.DiseaseID = d.DiseaseID
        join Reports r on rd.ReportID = r.ReportID
        where r.ReportID = %s
    """

    data = (reportId,)    
    cursor.execute(query, data)
    results = cursor.fetchall()

    diseases = []
    for disease in results:
        diseases.append(disease[0].lower())

    return diseases

def getSyndromesForReport(reportId, cursor, key_terms=None):
    query = """
        SELECT s.SyndromeName
        FROM Syndromes s
        join Report_Syndromes rs on rs.SyndromeID = s.SyndromeID
        join Reports r on rs.ReportID = r.ReportID
        where r.ReportID = %s
    """

    data = (reportId,)
    
    cursor.execute(query, data)
    results = cursor.fetchall()

    syndromes = []
    for syndrome in results:
        syndromes.append(syndrome[0].lower())

    return syndromes

def getKeywordsForReport(reportId, cursor):
    query = """
        SELECT k.Keyword
        FROM Keywords k
        join Report_Keywords rk on rk.KeywordID = k.KeywordID
        join Reports r on rk.ReportID = r.ReportID
        where r.ReportID = %s
    """
    
    data = (reportId,)
    
    cursor.execute(query, data)
    results = cursor.fetchall()

    keywords = []
    for keyword in results:
        keywords.append(keyword[0].lower())

    return keywords

def addLog(results):
    log = {
        "team_name": "McNuggets",
        "accessed_time": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        "data_source": "promedmail.org"
    }

    response = {
        "log": log,
        "response": results
    }

    return response


if __name__ == "__main__":
    app.run()