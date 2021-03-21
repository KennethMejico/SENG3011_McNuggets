"""
A web scraper to crawl and scrape all the articles on promedmail.org.
Can then dump all the articles and information into a PostgreSQL database
"""

# IMPORTS
# External Imports
import requests
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

    # REQUEST URL
    url = "https://promedmail.org/wp-admin/admin-ajax.php"

    # DATA REQUEST
    data = {
        'action' 	:   'get_latest_posts',
        'edate' 	: 	edate,
        'return_map': 	return_map,
        'feed_id' 	: 	feed_id,
        'seltype' 	: 	seltype,
        'keyword'	: 	keyword,
        'diesesIds'	:   diesesIds
    }

    # HEADER FOR REQUEST
    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }

    #json response for processing
    jsonResponse = ""

    def __init__ (self):
        pass

    def fetch(self):
        response = requests.post(self.url, self.data, headers=self.headers)
        self.jsonResponse = response.json()

    def process(self):
        print("Processing Data Now")
        # helpers.processData(self.jsonResponse)
        db_controller.writeToDB(self.jsonResponse)
        print("Data Proccessed")

    def run(self):
        self.fetch()
        self.process()




#TESTING
if __name__ == "__main__":
    scraper = Scraper()
    scraper.run()
