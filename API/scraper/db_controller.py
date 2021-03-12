# import psycopg2
import mysql.connector # pip3 install mysql-connector-python
import helpers

# change this to your own config for now until we set up on AWS
db = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="password",
    database="seng_mcnuggets"
)
cursor = db.cursor()

def writeToDB():
    pass

def insertLocations(locationId):
    query = "INSERT INTO Locations (LocationID, Latitude, Longitude, LocationName) VALUES (%d, %f, %f, %s)"

    # method 1 - inserting everything at once, will be faster than hitting the db for every row of data we need to insert
    locationData = [
        (locationId, latitude, longitude, locationName),
    ] # example - need to get list from somewhere
    cursor.executemany(query, values)

    # method 2 inserting one row at a time
    data = (locationId, latitude, longitude, locationName)
    cursor.execute(query, data)

    db.commit()
    print(cursor.rowcount, "was inserted")
