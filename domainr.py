import urllib2
import json

def domainr_search_json(domainname):
	requesturl = 'https://domainr.com/api/json/search?client_id=python_davemenninger&q='
	requesturl += domainname
	request = urllib2.Request(requesturl)
	request.add_header('User-Agent', 'domainr.py/0.1')
	opener = urllib2.build_opener()
	response = opener.open(request).read()
	objs = json.loads(response)
	return objs

def is_com_taken(domainr_json):
	return domainr_json['results'][0]['availability'] == 'taken'

def is_net_taken(domainr_json):
	return domainr_json['results'][1]['availability'] == 'taken'

def is_org_taken(domainr_json):
	return domainr_json['results'][2]['availability'] == 'taken'
