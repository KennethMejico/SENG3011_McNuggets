"""
A web scraper to crawl and scrape all the articles on promedmail.org.
Can then dump all the articles and information into a PostgreSQL database
"""

# IMPORTS
# External Imports
import requests
# Scraper Helpers Import
from . import helpers

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

""" data2 = {
    'action' : 'get_latest_post_data',
    'alertId': response['first_alert'],
} """


#TESTING
if __name__ == "__main__":
    response = requests.post(url, data, headers=headers)
    jsonResponse = response.json()
    print("Processing Data Now")
    helpers.processData(jsonResponse)
    print("Data Proccessed")