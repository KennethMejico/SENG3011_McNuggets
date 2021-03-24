'''
This test file is for the internal API endpoints
'''
#py -m pytest Phase_1\TestScripts\APITests.py

import json
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

def test_search(setup):
    #print(client.get("/"))
    print(APIController.search("2016-12-10T23:59:59", "2016-12-20T23:59:59", "Sydney, New South Wales, Australia", "Measles", db_manager.getDbConnection()))
    assert 1 == 0