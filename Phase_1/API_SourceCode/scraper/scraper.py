"""
A web scraper to crawl and scrape all the articles on promedmail.org.
Can then dump all the articles and information into a PostgreSQL database
"""

import re
from datetime import date as Date
import time
import requests
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta

#import db_controller as db_controller
import sys
import os

import helpers
sys.path.append(os.path.abspath("Phase_1/API_SourceCode/"))
from APIController import db_controller


class Scraper:
    """
        A scraper Class. Use the Run method to run it after initilzing it.
        >>> url is the url that the endpoint is located at
        >>> data is the data format of the data request
        >>> header is the header format of the data request
    """
    # DATA VALUES
    edate 			= ''
    return_map 		= ''
    feed_id 		= 1
    seltype 		= 'latest'
    postHeading	    = ''
    keyword         = ''
    diesesIds 	    = ''

    possibleSymptoms = [
        'pain', 'chills', 'fever', 'paresthesia', 'numbness', 'dizzy', 'dizziness', 'dry mouth', 'mouth dry', 'nausea', 'breath shortness',
        'short of breath', 'sleepy', 'febrile onset', 'headache', 'vomiting', 'tiredness', 'jaundice', 'mild symptoms', 'thirsty', 'weak', 'sweaty', 'thirst',
        'irregular breathing', 'impaired breathing', 'hearing loss', 'vision loss', 'itchiness', 'rash', 'blindness', 'taste', 'impaired speech', 'blurred vision',
        'muscle weakness', 'swelling', 'fatigue', 'pyrexia', 'shivering', 'malaise', 'arrythmia', 'chest pain', 'bradycardia', 'palpitations', 'halitosis', 'sore throat',
        'bleeding', 'constipation', 'diarrhea', 'hematochezia', 'fecal incontinence','blisters', 'edema', 'ataxia', 'confusion', 'phobia', 'pelvic pain', 'stiffness', 'insomnia',
        'unconsciousness', 'hallucination', 'muscle cramps', 'paralysis', 'sores', 'abrasion', 'cough', 'sneeze', 'sneezing', 'flu-like symptoms', 'running nose', 'seizures', 
        'delirium','coma', 'brain damage', 'death', 'mucas'
    ]

    debugging = False

    # REQUEST URL
    url = "https://promedmail.org/wp-admin/admin-ajax.php"
    data = {
        'action' 	:   'get_latest_posts',
        'edate' 	: 	edate,
        'return_map': 	return_map,
        'feed_id' 	: 	feed_id,
        'seltype' 	: 	seltype,
        'keyword'	: 	keyword,
        'diesesIds'	:   diesesIds
    }
    """ data2 = {
        'action' : 'get_latest_post_data',
        'alertId': response['first_alert'],
    } """

    # HEADER FOR REQUEST
    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }

    def __init__ (self):
        pass

    def findDate(self, string):
        """Finds the date of an article for the string format returned by promedmail.org"""
        return re.search('^.+(?= <a h)|$', string).group()

    def findID(self, string):
        """Finds the id of an article for the string format returned by promedmail.org"""
        return re.search('(?<=id=\"id)\d+(?=\")|$', string).group()

    def findName(self, string):
        """Finds the name of an article for the string format returned by promedmail.org"""
        try:
            return re.search('<a.*> ?(.+?)</a>', string).group(1)
        except:
            if self.debugging:
                print(string)
            return ""

    def printInfo(self, key, date, aid, name):
        """
        Prints data for the given information in the following format:
        >>> Location Key: {key}.    Article Date: {date}.
        >>> Article ID: {aid}.    Article Name: {name}.
        """
        print(f"Location Key: {key}.    Article Date: {date}.   Article ID: {aid}.    Article Name: {name}.")

    def generateReports(self, dbConn, articleDate, articleID, articleMarkerID, articleName, articleText):
        """
            Generates reports and inserts it into a database
            >>> self is a scraper object
            >>> dbConn is a database connection object
            >>> articleDate is the date from the article
            >>> articleMarkerID is the marker ID from an article
            >>> articleName is the name of the article
            >>> articleText is the text of the article
        """
        LAN = articleName.lower()
        # If it contains announcement, that means it isn't a health thing
        if 'announcement' in LAN:
            return
        
        # If the title contains unknown, undiagnosed that means it is an unknown cause of disease.
        # Else the title of the disease is in the title
        if 'undiagnosed' in LAN or 'unknown' in LAN:
            diseaseType = 'unknown'
        else:
            diseaseType = LAN.split(':')[0]
            diseaseType = re.sub("[\(\[].*?[\)\]]", "", diseaseType)
            diseaseType = re.sub('update', '', diseaseType)
        
        symptoms = []
        for symptom in self.possibleSymptoms:
            if symptom in articleText:
                symptoms.append(symptom)

        eventDate = articleDate
        locationID = articleMarkerID

        print (f"Disease Type: {diseaseType}  ||  Report Date: {str(eventDate)}  ||  Location ID: {str(locationID)}  ||  Symptoms:  {symptoms}")
        db_controller.reportToDB(dbConn, articleID, diseaseType, eventDate, locationID, symptoms)

    def processData(self, dbConn, response):
        """Processes data for the JSON response given by promedmail.org"""
        contents = response['contents']
        lastDate = Date.today()
        updates = False
        for key in sorted(contents):
            markerID = key
            db_controller.markerToDB(dbConn, markerID, response['markers'][markerID])
            
            for item in contents[key]:
                date  = self.findDate(item)
                aid   = self.findID(item)
                
                # self.printInfo(key, date, aid, name)
                tempDate = Date.fromtimestamp(time.mktime(time.strptime(date, "%d %b %Y")))
                
                if tempDate < lastDate:
                    lastDate = tempDate
                
                if db_controller.idInDB(dbConn, aid): 
                    # This returns true if the article is already in db, therefore skip it
                    continue
                
                updates = True
                name  = self.findName(item)
                dataReq = {
                    'action' : 'get_latest_post_data',
                    'alertId': aid,
                }
                soup = BeautifulSoup(requests.post(self.url, dataReq, headers=self.headers).json()['post'], "html5lib")
                text = soup.find('div', attrs={'class':'text1'}).get_text(separator=" ")
                
                db_controller.articleToDB(dbConn, markerID, date, aid, name, text)

                self.generateReports(dbConn, tempDate, aid, markerID, name, text)

        dbConn.commit()
        return (lastDate, len(contents), updates)

    def fetch(self, edate):
        """ Makes a data request to a the promedmail database, for a specific date given by edate """
        # DATA REQUEST
        data = {
            'action' 	:   'get_latest_posts',
            'edate' 	: 	edate,
            'return_map': 	self.return_map,
            'feed_id' 	: 	self.feed_id,
            'seltype' 	: 	self.seltype,
            'keyword'	: 	self.keyword,
            'diesesIds'	:   self.diesesIds
        }
        response = requests.post(self.url, data, headers=self.headers)
        return response.json()

    def run(self):
        dbConn = db_controller.getDbConnection()
        edate = ''
        jsonResponse = self.fetch(edate)
        if db_controller.idInDB(dbConn, jsonResponse['first_alert']):
            return
        
        while (jsonResponse['contents']):
            rdate, responseCount, updates = self.processData(dbConn, jsonResponse)
            if self.debugging:
                print(str(rdate))
            if updates == False:
                break
            if rdate == Date.today():
                break
            if responseCount == 1:
                rdate += relativedelta(months=-6)
            edate = str(rdate)
            jsonResponse = self.fetch(edate)

        dbConn.close()

    def getLatest(self):
        jsonresponse = self.fetch('')
        dataReq = {
                    'action' : 'get_latest_post_data',
                    'alertId': jsonresponse['first_alert'],
                }
        soup = BeautifulSoup(requests.post(self.url, dataReq, headers=self.headers).json()['post'], "html5lib")
        print(soup.find('div', attrs={'class':'text1'}).get_text(separator=" "))

    def fetchFeedID(self, feed_id):
        data = {
            'action' 	:   'get_latest_posts',
            'edate' 	: 	'',
            'return_map': 	self.return_map,
            'feed_id' 	: 	feed_id,
            'seltype' 	: 	self.seltype,
            'keyword'	: 	self.keyword,
            'diesesIds'	:   self.diesesIds
        }
        response = requests.post(self.url, data, headers=self.headers)
        return response.json()
    
    def fetchOneEachFeed(self):
        for i in range(0, 255, 1):
            print("FEED " + str(i))
            response = self.fetchFeedID(i)
            dataReq = {
                    'action' : 'get_latest_post_data',
                    'alertId': response['first_alert'],
                }
            try :
                soup = BeautifulSoup(requests.post(self.url, dataReq, headers=self.headers).json()['post'], "html5lib")
                print(soup.get_text(separator=" "))
            except:
                print("Error")
            finally:
                print("\n\n\n\n\n\n\n")
    
    def fetchTopicalID(self, feed_id):
        data = {
            'action' 	:   'get_latest_posts',
            'edate' 	: 	'',
            'return_map': 	self.return_map,
            'feed_id' 	: 	feed_id,
            'seltype' 	: 	'topical',
            'keyword'	: 	self.keyword,
            'diesesIds'	:   self.diesesIds
        }
        response = requests.post(self.url, data, headers=self.headers)
        return response.json()

    def fetchTopicalOneEachFeed(self):
        for i in range(0, 255, 1):
            print("FEED " + str(i) + "\n")
            response = self.fetchTopicalID(i)
            dataReq = {
                    'action' : 'get_latest_post_data',
                    'alertId': response['first_alert'],
                }
            try :
                soup = BeautifulSoup(requests.post(self.url, dataReq, headers=self.headers).json()['post'], "html5lib")
                print(soup.get_text(separator=" "))
            except:
                print("Error")
            finally:
                print("\n\n\n\n\n\n\n")
        
    def fetchSimple(self):
        response = requests.post(self.url, self.data, headers=self.headers)
        self.jsonResponse = response.json()

    def processSimple(self):
        print("Processing Data Now")
        # helpers.processData(self.jsonResponse)
        db_controller.writeToDB(self.jsonResponse)
        print("Data Proccessed")

    def runSimple(self):
        self.fetchSimple()
        self.processSimple()

if __name__ == "__main__":
    # Testing
    sc = Scraper()
    sc.run()