# import psycopg2
import mysql.connector # pip3 install mysql-connector-python

# change this to your own config for now until we set up on AWS
db = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="password",
    database="seng_mcnuggets"
)
cursor = db.cursor()

def writeToDB(jsonResponse):
    insertLocations(jsonResponse)

def insertLocations(jsonResponse):
    """Writes location data from the JSON response to db"""
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
    cursor.executemany(query, results)
    db.commit()
    print(cursor.rowcount, "was inserted")
    