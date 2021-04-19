# Scraper that scrapes data from covidlive.com.au # Data includes: 
# - average of last 7 local cases in given state 
# - latest local case number in given state
# =======================
# Writes data to file named covidData.txt
# usage: python3 covidCasesScraper.py

import requests_cache
import json
import re
from statistics import mean
from bs4 import BeautifulSoup
from datetime import date

def getLocalCases(state):
    URL = 'https://covidlive.com.au/report/daily-source-overseas/{}'.format(state)
    session = requests_cache.CachedSession('demo_cache')
    page = session.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    local_cases = soup.find_all('td', class_="COL4 NET")
    first_10_local = local_cases[103:110] # 6 Jan 2021
    cases = []
    for case in first_10_local:
        num = re.search('(<span>|<span class="red">|<span class="green">)(.*)</span>', str(case))
        cases.append(int(num.group(2)))
    return cases
    
def statesCases():
    states = ['nsw', 'qld', 'vic', 'wa', 'sa', 'tas', 'act', 'nt']
    stateCasesDict = {}
    for state in states:
        cases = getLocalCases(state)
        avg = mean(cases)
        avg = "{:.2f}".format(avg)
        latest = cases[0]
        stateCasesDict[state] = {'average': avg, 'latest': latest, 'curTime': "2020-06-20"} # str(date.today())} Date hardcoded
    return stateCasesDict
    
if __name__ == "__main__":
    with open('covid19Data.json', 'w') as outfile:
        json.dump(statesCases(), outfile, indent=4, sort_keys=True)