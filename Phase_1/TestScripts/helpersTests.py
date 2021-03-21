import pytest
import json
import sys, os
sys.path.append(os.path.abspath("API/scraper"))
from helpers import *
# py -m pytest Phase_1\TestScripts\helpersTests.py

@pytest.fixture()
def setup():
    res1 = "28 Feb 2021 <a href=\"javascript:;\" id=\"id8219231\" class=\"bcl\"> Ebola update (20): USA, Guinea, Sub-Saharan Africa</a>"
    res2 = "01 Sep 2020 <a href=\"javascript:;\" id=\"id7823938\" class=\"bcl\"> Announcement (04): ProMED anniversary award 2020</a>"
    return {"res1": res1, "res2": res2, "scraper": Scraper()}

def test_findDate(setup):
    assert(findDate(setup["res1"]) == "28 Feb 2021")
    assert(findDate(setup["res2"]) == "01 Sep 2020")

def test_findID(setup):
    assert(findID(setup["res1"]) == "8219231")
    assert(findID(setup["res2"]) == "7823938")

def test_findName(setup):
    assert(findName(setup["res1"]) == "Ebola update (20): USA, Guinea, Sub-Saharan Africa")
    assert(findName(setup["res2"]) == "Announcement (04): ProMED anniversary award 2020")

def test_printInfo(capsys):
    printInfo(100, "28 Feb 2021", "8219231", "Ebola update (20): USA, Guinea, Sub-Saharan Africa")
    out, err = capsys.readouterr()
    assert(out ==  "Location Key: 100.    Article Date: 28 Feb 2021.    Article ID: 8219231.    Article Name: Ebola update (20): USA, Guinea, Sub-Saharan Africa.\n")

def test_processData(capsys):
    with open("Phase_1\\TestScripts\\processDataInput.json", "r") as input_file:
        raw_data = json.load(input_file)
    processData(raw_data)
    out, err = capsys.readouterr()
    with open("Phase_1\\TestScripts\\processDataOutput.txt", "r") as output_file:
        expData = output_file.read()  + "\n"
    assert(out == expData)