'''
This test file is for the endpoints on the live deployment
'''
#py -m pytest Phase_1\TestScripts\endpointTests.py

import pytest
from datetime import datetime
import json
import sys
import os
import requests
sys.path.append(os.path.abspath("Phase_1/API_SourceCode/scraper"))
from helpers import *
import db_manager
import db_controller

# Not all of these will be implemented most likely

def sort_json(obj):
    # https://stackoverflow.com/a/25851972
    if isinstance(obj, dict):
        return sort_json((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sort_json(ordered(x) for x in obj)
    else:
        return obj

@pytest.fixture()
def setup():
    db_manager.setup()
    yield
    db_manager.teardown()

def test_database():
    '''
    Tests that the database connection is working
    '''
    server = db_manager.getServerConnection()
    cur = server.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS testmcnuggetsdb")
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
    assert result[0] == 1 and result[1] == "Sydney" and len(result) == 2

def validLog(json):
    assert(json["log"]["team_name"] == "McNuggets")
    assert(json["log"]["data_source"] == "promedmail.org")
    assert((datetime.now() - datetime.strptime(json["log"]["accessed_time"], '%Y-%m-%dT%H:%M:%S')).total_seconds() <= 1)

def test_logging():
    validLog(requests.get("https://4k6yve9rsa.execute-api.ap-southeast-2.amazonaws.com/default/mcnuggets/list/diseases").json())

def test_noParams():
    parameters = {}
    r = requests.get("https://4k6yve9rsa.execute-api.ap-southeast-2.amazonaws.com/default/mcnuggets/search", params=parameters)
    assert r.json()["response"] == "Please input a start and end date."

    r = requests.get("https://4k6yve9rsa.execute-api.ap-southeast-2.amazonaws.com/default/mcnuggets/count", params=parameters)
    assert r.json()["response"] == "Please input a start and end date."

def test_badParams():
    parameters = {
        "from_date": "2017-01-01T00:00:00"
    }
    r = requests.get("https://4k6yve9rsa.execute-api.ap-southeast-2.amazonaws.com/default/mcnuggets/search", params=parameters)
    assert r.json()["response"] == "Please input a start and end date."

    r = requests.get("https://4k6yve9rsa.execute-api.ap-southeast-2.amazonaws.com/default/mcnuggets/count", params=parameters)
    assert r.json()["response"] == "Please input a start and end date."

    parameters = {
        "to_date": "2017-01-01T00:00:00"
    }
    r = requests.get("https://4k6yve9rsa.execute-api.ap-southeast-2.amazonaws.com/default/mcnuggets/search", params=parameters)
    assert r.json()["response"] == "Please input a start and end date."

    r = requests.get("https://4k6yve9rsa.execute-api.ap-southeast-2.amazonaws.com/default/mcnuggets/count", params=parameters)
    assert r.json()["response"] == "Please input a start and end date."

def test_search():
    parameters = {
        "start_date": "2018-01-01T00:00:00",
        "end_date": "2019-01-01T00:00:00",
        "location": "Australia",
        "key_terms": "Gangrene,Buruli Ulcer",
        "timezone": "+11"
    }
    r = requests.get("https://4k6yve9rsa.execute-api.ap-southeast-2.amazonaws.com/default/mcnuggets/search", params=parameters)
    # Fails because of timeout
    print(r.json())
    assert len(r.json()["response"]) == 2
    # Should get two results
    # https://www.theage.com.au/national/victoria/flesh-eating-ulcer-cases-rapidly-increase-spread-on-victorian-coast-20181020-p50ax6.html
    # https://www.9news.com.au/national/girl-struck-down-with-mystery-flesh-eating-disease-in-victoria/36a70de7-286f-4f7e-99af-9d18d6559904

def test_listDiseases():
    with open("Phase_1/API_SourceCode/jsonFiles/disease_list.json", "r") as f:
        expected = json.load(f)
    # Call API, put the response json in response
    r = requests.get("https://4k6yve9rsa.execute-api.ap-southeast-2.amazonaws.com/default/mcnuggets/list/diseases")
    # Format no longer used
    assert(sort_json(expected) == sort_json(r.json()["response"]))

def test_listSyndromes():
    with open("Phase_1/API_SourceCode/jsonFiles/syndrome_list.json", "r") as f:
        expected = json.load(f)
    # Call API, put the response json in response
    r = requests.get("https://4k6yve9rsa.execute-api.ap-southeast-2.amazonaws.com/default/mcnuggets/list/syndromes")
    # Format no longer used
    assert(sort_json(expected) == sort_json(r.json()["response"]))

def test_listKeywords():
    with open("Phase_1/API_SourceCode/jsonFiles/keyword_list.json", "r") as f:
        expected = json.load(f)
    # Call API, put the response json in response
    r = requests.get("https://4k6yve9rsa.execute-api.ap-southeast-2.amazonaws.com/default/mcnuggets/list/keywords")
    # Format no longer used
    assert(sort_json(expected) == sort_json(r.json()["response"]))

def test_listLocations():
    # I have no idea what this will return
    pass

def test_listReports():
    pass

def test_count():
    parameters = {
        "start_date": "2021-2-24T23:59:59",
        "end_date": "2021-2-25T23:59:59",
    }
    r = requests.get("https://4k6yve9rsa.execute-api.ap-southeast-2.amazonaws.com/default/mcnuggets/count", params=parameters)
    r2 = requests.get("https://4k6yve9rsa.execute-api.ap-southeast-2.amazonaws.com/default/mcnuggets/search", params=parameters)
    assert(r.json()["response"] == {"salmonellosis, st typhimurium - usa": 1, "covid-19  ": 1, "foot & mouth disease - iran": 1, "salmonellosis, st enteritidis - canada": 1, "ebola  ": 1, "plague - congo dr": 1, "cholera, diarrhea & dysentery  ": 1, "salmonellosis - uk": 1})