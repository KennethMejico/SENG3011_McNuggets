import re

def findDate(string):
    return re.search('^.+(?= <a h)|$', string).group()

def findID(string):
    return re.search('(?<=id=\"id)\d+(?=\")|$', string).group()

def findName(string):
    return re.search('<a.*> (.+?)</a>', string).group(1)

def printInfo(key, date, aid, name):
    print(f"Location Key: {key}.    Article Date: {date}.\
        Article ID: {aid}.    Article Name: {name}.")

def processData(jsonResponse):
    contents = jsonResponse['contents']
    for key in contents:
        for item in contents[key]:
            date  = findDate(item)
            aid   = findID(item)
            name  = findName(item)
            printInfo(key, date, aid, name)
    pass
