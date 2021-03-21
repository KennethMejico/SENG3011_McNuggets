"""
A web scraper to crawl and scrape all the articles on promedmail.org.
Can then dump all the articles and information into a PostgreSQL database
"""

import re
from datetime import date as Date
import time
import requests
from bs4 import BeautifulSoup

#import db_controller as db_controller

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

    # REQUEST URL
    url = "https://promedmail.org/wp-admin/admin-ajax.php"

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
        return re.search('<a.*> (.+?)</a>', string).group(1)

    def printInfo(self, key, date, aid, name):
        """
        Prints data for the given information in the following format:
        >>> Location Key: {key}.    Article Date: {date}.
        >>> Article ID: {aid}.    Article Name: {name}.
        """
        print(f"Location Key: {key}.    Article Date: {date}.\
            Article ID: {aid}.    Article Name: {name}.")

    def generateReports(self, articleDate, articleID, articleMarkerID, articleName, articleText):
        pass

    def processData(self, response):
        """Processes data for the JSON response given by promedmail.org"""
        contents = response['contents']
        lastDate = Date.today()
        for key in contents:
            markerID = key
            # db_controller.addMarker(markerID, response['markers'][markerID])  # TODO write to DB
            for item in contents[key]:
                date  = self.findDate(item)
                aid   = self.findID(item)
                name  = self.findName(item)
                # self.printInfo(markerID, date, aid, name)                     # FOR DEBUGGING. REMOVE IN PRODUCTION # TODO
                tempDate = Date.fromtimestamp(time.mktime(time.strptime(date, "%d %b %Y")))
                if tempDate < lastDate:
                    lastDate = tempDate
                dataReq = {
                    'action' : 'get_latest_post_data',
                    'alertId': aid,
                }
                soup = BeautifulSoup(requests.post(self.url, dataReq, headers=self.headers).json()['post'], "html5lib")
                text = soup.find('div', attrs={'class':'text1'}).get_text(separator=" ")
                # print(text + "\n\n\n\n")                                      # FOR DEBUGGING. REMOVE IN PRODUCTION # TODO
                
                # db_controller.writeToDB(markerID, date, aid, name, text)      # TODO write to DB

                self.generateReports(date, aid, markerID, name, text)
        return lastDate
                

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
        edate = ''
        jsonResponse = self.fetch(edate)
        while (jsonResponse['contents'].keys()):
            rdate = self.processData(jsonResponse)
            if rdate == Date.today():
                break
            edate = rdate.year + '-' + rdate.month + '-' + rdate.day
            jsonResponse = self.fetch(edate)

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
        



#TESTING
if __name__ == "__main__":
    scraper = Scraper()
    scraper.fetchTopicalOneEachFeed()
