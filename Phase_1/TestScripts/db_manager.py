import mysql.connector
import sys
import os

sys.path.append(os.path.abspath("Phase_1/API_SourceCode/"))

import db_controller

def getServerConnection():
    server = mysql.connector.connect(
        host="mcnuggetsdb.ckxxjj5qvkgp.ap-southeast-2.rds.amazonaws.com",
        port="3306",
        user="McNuggetsAdmin",
        password="Boysenberry"

    )
    return server

def getDbConnection():
    mydb = mysql.connector.connect(
        host="mcnuggetsdb.ckxxjj5qvkgp.ap-southeast-2.rds.amazonaws.com",
        port="3306",
        user="McNuggetsAdmin",
        password="Boysenberry",
        database="mcnuggetsdb"
    )
    return mydb

def setup():
    serverConn = getServerConnection()
    cursor = serverConn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS mcnuggetsdb")
    serverConn.close()

    dbConn = getDbConnection()
    db_controller.executeSchema(dbConn)

    insertLocations(dbConn)
    insertArticles(dbConn)
    insertReports(dbConn)

    dbConn.close()
    print("set up complete")

def teardown():
    serverConn = getServerConnection()
    cursor = serverConn.cursor()

    query = "DROP DATABASE mcnuggetsdb"
    cursor.execute(query)

    serverConn.close()
    print("test database deleted")

def insertLocations(dbConn):
    cursor = dbConn.cursor()
    query = "INSERT IGNORE INTO Locations (LocationID, Latitude, Longitude, LocationName) VALUES (%s, %s, %s, %s)"
    data = [
        ("1", "-33.826391", "151.199005", "Sydney, New South Wales, Australia"),
        ("2", "-27.451348", "153.027494", "Brisbane, Queensland, Australia"),
        ("3", "40.041929", "116.483688", "Beijing, China"),
        ("4", "40.710143", "-74.003897", "New York City, New York, United States"),
        ("5", "51.510362", "-0.133210", "London, United Kingdom"),
        ("6", "35.693000", "139.771806", "Tokyo, Japan"),
        ("7", "35.652499", "139.738272", "Minato City, Tokyo, Japan")
    ]
    cursor.executemany(query, data)
    dbConn.commit()

def insertArticles(dbConn):
    cursor = dbConn.cursor()
    query = "INSERT IGNORE INTO Articles (ArticleID, PubDate, ArticleName, MainText, LinkToArticle) VALUES (%s, %s, %s, %s, %s)"
    data = [
        ("1", "2016-12-16", "Measles Update: Australia Sydney", """Measles warning for Sydney after 3 infectious adults visit multiple locations
-----------------------------------------------------------------------------
Health authorities have warned the public to be on alert for measles symptoms after 3 people contracted the highly contagious disease in Sydney this month [December 2016].

All 3 adults spent considerable time in the Sydney metropolitan area while they were infectious, NSW [New South Wales] Health reported on Friday [16 Dec 2016].

Health experts continue to warn people to check they have been immunised against measles. For further information visit: https://www.betterhealth.vic.gov.au/

The 3 cases visited multiple locations between 26 Nov and 15 Dec [2016] including:
- Inner city hospital emergency departments
- GP clinics and medical centres in George Street, Sydney, Darlinghurst, Leichhardt, Camperdown and Bondi
- Restaurants and shops in the CBD, Ultimo, Bondi, Bondi Junction, Leichhardt, Double Bay, Chatswood and Marrickville
- Public transport on routes in the centre, north and east of the city.
""", "www.some_url.com"),
        ("2", "2020-03-21", "COVID Update: Minato City Tokyo Japan", "New COVID infections: 500 found in Minato City of Tokyo, They were seen around these places", "www.someurl/minato"),
        ("3", "2020-08-28", "COVID Update: Tokyo Japan", "New COVID infections: 2000 found in Tokyo, Please get tested if you are feeling any of the symptoms", "www.someurl/tokyo"),
    ]
    cursor.executemany(query, data)
    dbConn.commit()

def insertReports(dbConn):
    cursor = dbConn.cursor()

    report_query = "INSERT IGNORE INTO Reports (ReportID, ArticleID, EventDate) VALUES (%s, %s, %s)"
    report_data = [
        ("1", "1", "2016-12-16"),
        ("2", "2", "2020-02-21"),
        ("3", "3", "2020-08-28")
    ]
    cursor.executemany(report_query, report_data)
    dbConn.commit()

    location_query = "INSERT IGNORE INTO Report_Locations (ReportID, LocationID) VALUE (%s, %s)"
    location_data = [
        ("1", "1"),
        ("2", "7"),
        ("2", "6"),
        ("3", "6")
    ]
    cursor.executemany(location_query, location_data)

    disease_query = "INSERT IGNORE INTO Report_Diseases (ReportID, DiseaseID) VALUE (%s, %s)"
    disease_data = [
        ("1", db_controller.getDiseaseId(dbConn, "measles")),
        ("2", db_controller.getDiseaseId(dbConn, "COVID-19")),
        ("3", db_controller.getDiseaseId(dbConn, "COVID-19"))
    ]
    cursor.executemany(disease_query, disease_data)

    syndrome_query = "INSERT IGNORE INTO Report_Syndromes (ReportID, SyndromeID) VALUE (%s, %s)"
    syndrome_data = [
        ("1", db_controller.getSyndromeId(dbConn, "Acute fever and rash")),
        ("1", db_controller.getSyndromeId(dbConn, "Influenza-like illness")),
        ("2", db_controller.getSyndromeId(dbConn, "Influenza-like illness")),
        ("2", db_controller.getSyndromeId(dbConn, "Acute respiratory syndrome")),
        ("2", db_controller.getSyndromeId(dbConn, "Fever of unknown Origin")),
        ("3", db_controller.getSyndromeId(dbConn, "Influenza-like illness")),
        ("3", db_controller.getSyndromeId(dbConn, "Acute respiratory syndrome")),
        ("3", db_controller.getSyndromeId(dbConn, "Fever of unknown Origin"))
    ]
    cursor.executemany(syndrome_query, syndrome_data)

    dbConn.commit()
