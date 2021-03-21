'''
This test file is for the internal API endpoints
'''
#py -m pytest Phase_1\TestScripts\APITests.py

import db_manager
import sys
import os
import pytest

sys.path.append(os.path.abspath("Phase_1/API_SourceCode/"))
import APIController
import db_controller

@pytest.fixture()
def setup():
    db_manager.setup()
    yield
    db_manager.teardown()

@pytest.fixture
def client():
    APIController.app.config["TESTING"] = True
    with APIController.app.app_context():
        with app.test_client() as client:
            return client

def test_search(setup):
    #print(client.get("/"))
    print(APIController.search("2016-12-10T23:59:59", "2016-12-20T23:59:59", "Sydney, New South Wales, Australia", "Measles", db_manager.getDbConnection()))
    assert 1 == 0

def test_database():
    server = db_manager.getServerConnection()
    cur = server.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS mcnuggetsdb")
    server.close()
    db = db_manager.getDbConnection()
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS TestTable (
    LocationID INTEGER NOT NULL PRIMARY KEY,
    LocationName VARCHAR(100) NOT NULL);''')
    cursor.execute('''INSERT IGNORE INTO TestTable (LocationID, LocationName) VALUES (1, 'Sydney')''')
    cursor.execute('''SELECT * FROM TestTable''')
    result = cursor.fetchone()
    db.commit()
    db_manager.teardown()
    assert result[0] == 1 and result[1] == "Sydney"