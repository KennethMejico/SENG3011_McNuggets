"""
A document full of helper functions for processing json from promedmail.org.
It can process information and has some functions to help with debugging.
These are all just for the format from promedmail.org. There is no certainty it will work outside of this
"""

import re

def findDate(string):
    """Finds the date of an article for the string format returned by promedmail.org"""
    return re.search('^.+(?= <a h)|$', string).group()

def findID(string):
    """Finds the id of an article for the string format returned by promedmail.org"""
    return re.search('(?<=id=\"id)\d+(?=\")|$', string).group()

def findName(string):
    """Finds the name of an article for the string format returned by promedmail.org"""
    return re.search('<a.*> (.+?)</a>', string).group(1)

def printInfo(key, date, aid, name):
    """
    Prints data for the given information in the following format:
    >>> Location Key: {key}.    Article Date: {date}.
    >>> Article ID: {aid}.    Article Name: {name}.
    """
    print(f"Location Key: {key}.    Article Date: {date}.\
        Article ID: {aid}.    Article Name: {name}.")

def processData(jsonResponse):
    """Processes data for the JSON response given by promedmail.org"""
    contents = jsonResponse['contents']
    for key in contents:
        for item in contents[key]:
            date  = findDate(item)
            aid   = findID(item)
            name  = findName(item)
            printInfo(key, date, aid, name)
