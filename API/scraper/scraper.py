"""
A web scraper to crawl and scrape all the articles on promedmail.org.
Can then dump all the articles and information into a PostgreSQL database
"""

# IMPORTS
# External Imports
import requests
import re


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

    """ data2 = {
        'action' : 'get_latest_post_data',
        'alertId': response['first_alert'],
    } """

    # HEADER FOR REQUEST
    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }

    #json response for processing
    jsonResponse = ""

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

    def processData(self, response):
        """Processes data for the JSON response given by promedmail.org"""
        contents = jsonResponse['contents']
        for key in contents:
            for item in contents[key]:
                date  = findDate(item)
                aid   = findID(item)
                name  = findName(item)
                printInfo(key, date, aid, name)

    def fetch(self):
        response = requests.post(self.url, self.data, headers=self.headers)
        self.jsonResponse = response.json()
    
    def process(self):
        print("Processing Data Now")
        self.processData(self.jsonResponse)
        print("Data Proccessed")
    
    def run(self):
        self.fetch()
        self.process()
        



#TESTING
if __name__ == "__main__":
    scraper = Scraper()
    scraper.run()
