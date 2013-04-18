# -*- coding: utf-8 -*-

import requests
from lxml import html as lh
import time
import random

#Easily query API with requests module

def query_ADS(query):
	d={'dev_key':'8IIQgx5DrWZBwr2o', 'q': query, 'rows': 10, 'fl':'title,author', 'sort': 'CITED asc'}
	response=requests.get( "http://adslabs.org/adsabs/api/search/", params=d)
	print 'url: ', response.url, '\n'
	jsonfiles=response.json()
	print 'raw json: ', jsonfiles, '\n'
	records=jsonfiles['results']['docs']
	for i, x in enumerate(records):
		print i,x 

query_ADS('quasar')
		

# Grab a blog post

def get_blog_text(link):
	r=requests.get(link)
	tree=lh.fromstring(r.text)
	list_of_text= ["A GREAT BLOG BOST:  "]
	list_of_text+=tree.xpath('string(/html/head/title)')
	list_of_text+=tree.xpath('//p/text()|//p/a/text()')
	print list_of_text
	text=''.join(list_of_text)
	text=text.split()
	text=' '.join(text)
	text=text.encode('utf-8')
	return text[:4000]

##print get_blog_text('http://altbibl.io/dst4l/visualization-for-analysis-and-storytelling/')

#Make a baby spider with link depth of 1
#trick sites into thinking you're a person (could get you into trouble)

def get_and_follow_links(link):
	sites={}
	headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)'}
	# default header: 'User-Agent': 'python-requests/1.2.0'
	r=requests.get(link, headers=headers)
	tree=lh.fromstring(r.text)
	list_of_text=tree.xpath('//p/text()|//p/a/text()')
	text=''.join(list_of_text)
	text=text.encode('utf-8')
	sites[link]=text
	links=tree.xpath('//a/@href')
	for l in links[10:15]:
		r=requests.get(l, headers=headers)
		tree=lh.fromstring(r.text)
		list_of_text=tree.xpath('//p/text()|//p/a/text()')
		text=''.join(list_of_text)
		text=text.split()
		text=' '.join(text)
		text=text.encode('utf-8')
		sites[l]=text
	for i, x in enumerate(sites.items()):
		print i, x

##links= get_and_follow_links('http://altbibl.io/dst4l/visualization-for-analysis-and-storytelling/')

