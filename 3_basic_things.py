# -*- coding: utf-8 -*-

import requests
from lxml import html as lh
import time
import random

#you will probably need a query, a dev key, and a base url to access an api
#This is code to access the Smithsonian Astrophysics Database API. 
#If you have another API you want to access, check with their documentation.
# They will tell you how to acquire a dev key and what the base_url should be.

def query_ADS(query, dev, base_url):
	#Below is a python dictionary that tells the database on the receiving end 
	#exactly what your query is and what sort of information you want returned.
	d={'dev_key': dev, 'q': query, 'rows': 10, 'fl':'title,author', 'sort': 'CITED asc'}
	response=requests.get( base_url, params=d)
	#show the url that requests made from your base url + parameters
	print 'url: ', response.url, '\n'
	#return a json file, which requests will turn into a python data structure
	jsonfiles=response.json()
	print 'raw json: ', jsonfiles, '\n'
	#access only that part of the json that you are interested in
	records=jsonfiles['results']['docs']
	#print each record sequentially
	for i, x in enumerate(records):
		print i,x 

#example of calling the function with the query 'quasar':
query_ADS('quasar')


#here we scrape a single site with a generalized scraping pattern to get text
#if you have the time and want more accuracy, you can identify which parts of
#the html document you want to retrieve, and write xpath queries to grab them exclusively
# this function will return a string

def get_blog_text(link):
	r=requests.get(link)
	# we are creating a lxml 'tree' object from the html
	# that requests just returned from our link
	tree=lh.fromstring(r.text)
	#using the xpath language to grab the title
	list_of_text=tree.xpath('string(/html/head/title)')
	list_of_text+=' '
	#getting all text from website
	#this will be kind of messy and grab stuff you don't want
	list_of_text+= tree.xpath('//text()')
	# for more precision, you might want to use this more complicated xpath instead:
	#list_of_text+=tree.xpath('//p/descendant-or-self::text()|//p//following-sibling::*//text()')
	text=''.join(list_of_text)
	#the next 2 lines get rid of extra whitespace
	text=text.split()
	text=' '.join(text)
	text=text.encode('utf-8')
	return text

#example query getting text from blog entry
print get_blog_text('http://altbibl.io/dst4l/visualization-for-analysis-and-storytelling/')

#Make a baby spider with link depth of 1
#Make sure doing it is not against the terms of the website!
#Check first to see if they have an api!

def get_and_follow_links(initial_link, num_of_returned_links):
	# we will create a simple python dictionary with this function
	#that has a key as the url, and the corresponding value all of the
	#text grabbed from the page
	sites={}
	r=requests.get(initial_link)
	tree=lh.fromstring(r.text)
	#using the more complicated xpath query shown in the second function
	list_of_text=tree.xpath('//p/descendant-or-self::text()|//p//following-sibling::*//text()')
	text=''.join(list_of_text)
	#making sure your computer can render non-ascii characters by encoding in utf-8
	text=text.encode('utf-8')
	sites[link]=text
	links=tree.xpath('//a/@href')
	for l in links[0:num_of_returned_links:
		r=requests.get(l)
		tree=lh.fromstring(r.text)
		list_of_text=tree.xpath('//p/descendant-or-self::text()|//p//following-sibling::*//text()')
		text=''.join(list_of_text)
		text=text.split()
		text=' '.join(text)
		text=text.encode('utf-8')
		sites[l]=text
		#taking a quick break so the websites don't get annoyed at you for too many requests
		time.sleep(random.randint(5,15))
	for i, x in enumerate(sites.items()):
		print i, x

#example query
links= get_and_follow_links('http://altbibl.io/dst4l/visualization-for-analysis-and-storytelling/')

