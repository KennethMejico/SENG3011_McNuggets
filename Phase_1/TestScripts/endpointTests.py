import pytest
import json
sys.path.append(os.path.abspath("Phase_1/API_SourceCode/scraper"))
from helpers import *

# Not all of these will be implemented most likely

def sort_json(obj):
    # https://stackoverflow.com/a/25851972
    if isinstance(obj, dict):
        return sort_json((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sort_json(ordered(x) for x in obj)
    else:
        return obj

def test_search():
    params = {
        "from_date": "2017-01-01T00:00:00",
        "to_date": "2019-01-01T00:00:00",
        "location": "Australia",
        "key_terms": "Gangrene,Buruli Ulcer"
        "timezone": "+11"
    }
    # Should get two results
    # https://www.theage.com.au/national/victoria/flesh-eating-ulcer-cases-rapidly-increase-spread-on-victorian-coast-20181020-p50ax6.html
    # https://www.9news.com.au/national/girl-struck-down-with-mystery-flesh-eating-disease-in-victoria/36a70de7-286f-4f7e-99af-9d18d6559904

def test_listDiseases():
    with open("API\jsonFiles\disease_list.json", "r") as f:
        expected = json.load(f)
        response = json.load(f)
    # Call API, put the response json in response
    assert(sort_json(expected), sort_json(response))

def test_listSyndromes():
    with open("API\jsonFiles\disease_list.json", "r") as f:
        expected = json.load(f)
        response = json.load(f)
    # Call API, put the response json in response
    assert(sort_json(expected), sort_json(response))

def test_getDatabase():
    # I have no idea what this will return
    pass

def test_count():
    pass

def test_images():
    pass