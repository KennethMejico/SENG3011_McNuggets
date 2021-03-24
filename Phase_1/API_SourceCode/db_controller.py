# import psycopg2
import mysql.connector # pip3 install mysql-connector-python
import json
import re

testing = False
def setTest():
    global testing
    testing = True

def getDbConnection():
    # change this to your own config for now until we set up on AWS
    if (testing):
        db = mysql.connector.connect(
            host="mcnuggetsdb.ckxxjj5qvkgp.ap-southeast-2.rds.amazonaws.com",
            port="3306",
            user="McNuggetsAdmin",
            password="Boysenberry",
            database="testmcnuggetsdb"
        )
    else:
        db = mysql.connector.connect(
            host="mcnuggetsdb.ckxxjj5qvkgp.ap-southeast-2.rds.amazonaws.com",
            port="3306",
            user="McNuggetsAdmin",
            password="Boysenberry",
            database="mcnuggetsdb"
        )
    return db

def executeSchema(db):
    # with open('database_Schema.sql', 'r') as f:
    #     with db.cursor() as cursor:
    #         cursor.execute(f.read(), multi=True)
    #     db.commit()
    
    statement = ""
    with db.cursor() as cursor:
        for line in open('Phase_1/API_SourceCode/database_Schema.sql', 'r'):
            if re.match(r'--', line):  # ignore sql comment lines
                continue
            if not re.search(r';$', line):  # keep appending lines that don't end in ';'
                statement = statement + line
            else:  # when you get a line ending in ';' then exec statement and reset for next statement
                statement = statement + line
                cursor.execute(statement)
                statement = ""
    db.commit()

    with open('Phase_1/API_SourceCode/jsonFiles/disease_list.json', 'r') as f:
        diseases = json.load(f)
        results = []
        for disease in diseases:
            if getDiseaseId(db, disease["name"]) is None:
                results.append((disease["name"].lower(),))
        query = "INSERT INTO Diseases (DiseaseName) VALUE (%s)"
        with db.cursor() as cursor:
            cursor.executemany(query, results)
        db.commit()
    
    with open('Phase_1/API_SourceCode/jsonFiles/syndrome_list.json', 'r') as f:
        syndromes = json.load(f)
        results = []
        for syndrome in syndromes:
            if getSyndromeId(db, syndrome["name"]) is None:
                results.append((syndrome["name"].lower(),))
        query = "INSERT INTO Syndromes (SyndromeName) VALUE (%s)"
        with db.cursor() as cursor:
            cursor.executemany(query, results)
        db.commit()
    
    with open('Phase_1/API_SourceCode/jsonFiles/keyword_list.json', 'r') as f:
        keywords = json.load(f)
        results = []
        for keyword in keywords:
            if getKeywordId(db, keyword["name"]) is None:
                results.append((keyword["name"].lower(),))
        query = "INSERT INTO Keywords (Keyword) VALUE (%s)"
        with db.cursor() as cursor:
            cursor.executemany(query, results)
        db.commit()

def getDiseaseId(db, name):
    with db.cursor() as cursor:
        query = f'SELECT DiseaseID FROM Diseases WHERE DiseaseName = "{name.lower()}"'
        cursor.execute(query)
        result = cursor.fetchone()
        if result is None:
            return None
        else:
            return result[0]

def getSyndromeId(db, name):
    with db.cursor() as cursor:
        query = f'SELECT SyndromeId FROM Syndromes WHERE SyndromeName = "{name.lower()}"'
        cursor.execute(query)
        result = cursor.fetchone()
        if result is None:
            return None
        else:
            return result[0]

def getKeywordId(db, name):
    with db.cursor() as cursor:
        query = f'SELECT KeywordID FROM Keywords WHERE Keyword = "{name.lower()}"'
        cursor.execute(query)
        result = cursor.fetchone()
        if result is None:
            return None
        else:
            return result[0]

def writeToDB(jsonResponse):
    insertLocations(jsonResponse)

def insertLocations(jsonResponse):
    # Writes location data from the JSON response to db
    results = []
    locations = jsonResponse['markers']
    for key in locations:
        location = locations[key]
        name = location[1]
        latitude = location[2]
        longitude = location[3]
        results.append((
            key,
            latitude,
            longitude,
            name
        ))

    query = "INSERT IGNORE INTO Locations (LocationID, Latitude, Longitude, LocationName) VALUES (%s, %s, %s, %s)"
    dbConn = getDbConnection()
    cursor = dbConn.cursor()
    cursor.executemany(query, results)
    dbConn.commit()
    print(cursor.rowcount, "was inserted")
    dbConn.close()

def idInDB(dbConnection, articleID):
    commandOutput = None
    query = "SELECT ArticleID FROM Articles WHERE ArticleID=%s"
    cursor = dbConnection.cursor()
    cursor.execute(query, articleID)
    commandOutput = cursor.fetchone()
    return True if commandOutput is not None else False

def markerToDB(dbConnection, markerID, markerIDContents):
    # TODO
    pass

def articleToDB(dbConnection, markerID, date, aid, name, text):
    # TODO
    pass

def reportToDB(dbConnection, articleID, diseaseType, eventDate, locationID, symptoms):
    # TODO 
    pass