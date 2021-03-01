import re

def findDate(string):
    return re.search('$.+ \<|$', string).group()

def processData(jsonResponse):
    contents = jsonResponse['contents']
    for key in contents:
        for item in contents[key]:
            print(str(key), end=": ")
            """ date = findDate(item)
            print(date, end="") """
            print(item)
    pass
