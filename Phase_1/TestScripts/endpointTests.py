'''
This test file is for the endpoints on the live deployment
'''

import pytest
import json
import sys
import os
sys.path.append(os.path.abspath("Phase_1/API_SourceCode/scraper"))
from helpers import *
import db_manager

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
    print("hi")
    yield
    db_manager.teardown()
    print("bye")


def test_search(setup):
    params = {
        "from_date": "2017-01-01T00:00:00",
        "to_date": "2019-01-01T00:00:00",
        "location": "Australia",
        "key_terms": "Gangrene,Buruli Ulcer",
        "timezone": "+11"
    }
    # Should get two results
    # https://www.theage.com.au/national/victoria/flesh-eating-ulcer-cases-rapidly-increase-spread-on-victorian-coast-20181020-p50ax6.html
    # https://www.9news.com.au/national/girl-struck-down-with-mystery-flesh-eating-disease-in-victoria/36a70de7-286f-4f7e-99af-9d18d6559904

def test_listDiseases():
    with open("Phase_1/API_SourceCode/jsonFiles/disease_list.json", "r") as f:
        expected = json.load(f)
        response = expected
    # Call API, put the response json in response
    assert(sort_json(expected), sort_json(response))

def test_listSyndromes():
    with open("Phase_1/API_SourceCode/jsonFiles/syndrome_list.json", "r") as f:
        expected = json.load(f)
        response = expected
    # Call API, put the response json in response
    assert(sort_json(expected), sort_json(response))

def test_getDatabase(setup):
    # I have no idea what this will return
    pass

def test_count(setup):
    pass

def test_images(setup):
    pass