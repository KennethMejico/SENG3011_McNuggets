import requests
import json
import helpers

edate 			= ''
return_map 		= ''
feed_id 		= 1
seltype 		= 'latest'
postHeading	    = ''
keyword         = ''
diesesIds 	    = ''

url = "https://promedmail.org/wp-admin/admin-ajax.php"

request_type = 'post'
dataType    = 'json'

data = {
    'action' 	:   'get_latest_posts',
    'edate' 	: 	edate,
    'return_map': 	return_map,
    'feed_id' 	: 	feed_id,
    'seltype' 	: 	seltype,
    'keyword'	: 	keyword,
    'diesesIds'	:   diesesIds
}

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
}

""" data2 = {
    'action' : 'get_latest_post_data',
    'alertId': response['first_alert'],
} """


if __name__ == "__main__":
    response = requests.post(url, data, headers=headers)
    jsonResponse = response.json()
    print("Processing Data Now")
    helpers.processData(jsonResponse)
    print("Data Proccessed")
    
    """ f = open("scraper_output.json", "w")
    f.write("\n")
    f.write(json.dumps(jsonResponse, sort_keys=False, indent=4))
    f.close() """