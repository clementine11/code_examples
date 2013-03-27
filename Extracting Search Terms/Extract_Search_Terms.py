# -*- coding: utf-8 -*-

import sys
sys.path.append('/Users/alex/dropbox/Data_Science/Final_Project')
import re
import nltk
from nltk.corpus import stopwords
from bibstem_journal_dict import bibstemdict
from string import punctuation as punc
from nltk import bigrams
import freq_words
from collections import defaultdict


#use regular expressions and bigrams to formulate a series of likely search queries and feed them to the ADS API

#put ADS devkey here:

devkey= ''

text="""


Astronomers have discovered a new planet in our galaxy that is unlike any other found so far: Both the planet and its atmosphere are mostly water, though none of it is liquid.

The planet, GJ1214b, has a diameter 2.7 times that of Earth, and it weighs seven times as much. It probably has much more water than Earth — in the form of steam and a peculiar high-temperature ice that exists at extremely high pressures — and far less rock.

“There’s probably nothing too special about this planet itself,” said Zachory K. Berta, an astronomer at Harvard University who was involved with the research. The main thing, he added, is that “we have the opportunity to really see the density of the planet.”

He and his colleagues report their findings in The Astrophysical Journal.

To estimate the density and diameter, they measured the color of the light from the star that shines through the planet’s atmosphere.

“We’re observing the sunset on this planet,” he said.

Though the planet was discovered with a ground-based telescope, the data that allowed Mr. Berta and his colleagues to estimate the planet’s mass and density was gathered by the Hubble Space Telescope.

Looking ahead, the researchers have two goals. The first is to learn more about the planet.

“We’re going to study this atmosphere,” Mr. Berta said, “and work on the details so we can really try to understand what’s going on.” The second goal is to find more planets. Using the same techniques, the astronomers can study the atmosphere of other planets in detail, and Mr. Berta said a slightly smaller, slightly cooler planet might be capable of supporting life.

"""

text=text.replace('\n', ' ')

def match_names(text):
	#use nltk's named entity recognition to find person namesbut get rid of matches around word "not" (as in "not involved in the study")
	sentences=nltk.sent_tokenize(text)
	sentences=[nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]
	sentences=[nltk.ne_chunk(sent) for sent in sentences]
	names=[]
	for sent in sentences:
		for tree in sent:
			if str(tree)[1:7]=='PERSON':
				n=str(tree).replace('PERSON', '')
				n=n.replace('/NNP', '')
				n=n[1:-1]
				n=n.split()
				if len(n)>3:
					continue
				elif len(n)==1:
					continue
				else:
					names.append(' '.join(n))
	names=list(set(names))
	for name in names:
		x=re.search(r'.{120}'+name+'.{120}', text)
		if x:
			y=re.search(r'who was not', x.group())
			if y:
				y=y.group()
				names.remove(name)
	reorderednames=[]
	for name in names:
		name=name.split(' ')[-1]
		reorderednames.append(name)
	reorderednames=list(set(reorderednames))
	return reorderednames

def match_j_name(text):
	journal_names=re.compile(r'''Astronomical Journal|The Astrophysical Journal|Astronomical Review|Acta Astronomica
		|Astronomische Nachrichten|Bulletin of the American Astronomical Society|
		Ciel et Terre|Earth, Moon, and Planets|Journal of Astrophysics & Astronomy|Advances in Space Research|Science(?=\s*journal)|(?<=journal)\s*Science|Nature''')
	jnames=journal_names.findall(text)
	bibstems=[]
	for j in jnames:
		for key in bibstemdict.keys():
			if j.strip()==key:
				bibstems[len(bibstems):]=[bibstemdict[key].replace('.', '')]
				break
	return bibstems

def match_significant_numbers(text):
	#catches many names of astronomical objects
	nums=re.compile(r'[A-Z]{0,4}\s*[\d.-]{4,8}\s*[A-Z]{0,4}')
	names=re.compile((r'[A-Z]{1,5}\s*(?:[\d.-]{0,5}|\s*[A-Z]{0,4})'))
	nums=nums.findall(text)
	names=names.findall(text)
	names1=[x for x in names if len(x)>4]
	nums=nums[len(nums):]=names1
	return list(set(nums))

def guess_important_words(text):
	sw=stopwords.words('english')
	words=nltk.word_tokenize(text)
	words1=[w for w in words if w not in sw]
	words2=[w for w in words1 if len(w)>4]
	words3=[w.lower() for w in words2]
	for i in range(len(words3)):
		for p in punc:
			if p not in words3[i]:
				continue
			else:
				words3[i]=words3[i].replace(p, '')
	words4=[w for w in words3 if w not in freq_words.freq_words]
	fd={}
	for w in words4:
		if w in fd.keys():
			fd[w]=fd[w]+1
		else:
			fd[w]=1
	l= sorted(fd.items(), key=lambda x: x[1], reverse=True)
	trunc=[x for (x,y) in l if y>=3]
	return trunc

def guess_important_bigrams(text):
	sw=stopwords.words('english')
	words=nltk.word_tokenize(text)
	words1=[w for w in words if w not in sw]
	words2=[w for w in words1 if len(w)>=4]
	words3=[w.lower() for w in words2]
	for i in range(len(words3)):
		for p in punc:
			if p not in words3[i]:
				continue
			else:
				words3[i]=words3[i].replace(p, '')
	bg=bigrams(words3)
	fd={}
	for b in bg:
		if b in fd.keys():
			fd[b]=fd[b]+1
		else:
			fd[b]=1
	tups= sorted(fd.items(), key=lambda x: x[1], reverse=True)
	return [x+' '+ y for ((x,y),z) in tups]

def run_program(text):
	a=match_names(text)
	b=match_j_name(text)
	c=match_significant_numbers(text)
	d=guess_important_words(text)
	e=guess_important_bigrams(text)
	master_list=[]
	print "\nLikely names:\n", a
	print "\nBibstems:\n", b 
	print "\nPossibly important numbers and names:\n", c
	print "\nWords that appear 3 or more times: ", d
	print "\nFrequent bigrams: ", e[:3], "\n"
	querydict=dict([('bibstem', b), ('authors', a), ('bigrams', e), ('objectnames', c), ('freqwords', d)])
	return querydict

def query_generator(searchterms):
	import requests
	genlist=[]
	finalresults=[]
	if searchterms['bibstem']:
		qcombinations1=('bibstem:' + x + ' author:' +  ' ' + y + ' ' + z for x in searchterms['bibstem'] for y in searchterms['authors'] for z in searchterms['objectnames'][:3])
		genlist.append(qcombinations1)
		qcombinations2=('bibstem:' + x + ' author:' +  ' ' + y + ' ' for x in searchterms['bibstem'] for y in searchterms['authors'])
		genlist.append(qcombinations2)
		qcombinations3=('bibstem:' + x + ' author:' +  ' ' + y + ' ' + z for x in searchterms['bibstem'] for y in searchterms['authors'] for z in searchterms['freqwords'][:3])
		genlist.append(qcombinations3)
	elif searchterms['authors']:
		qcombinations2=('author:' +  ' ' + y + ' '  + z + ' ' + x for y in searchterms['authors'] for z in searchterms['objectnames'][:3] for x in searchterms['freqwords'][:3])
		genlist.append(qcombinations2)
		if searchterms['bigrams']:
			qcombinations3=(x+ ' '+ y+ ' ' for x in searchterms['freqwords'][:3] for y in searchterms['bigrams'][:3] )
			genlist.append(qcombinations3)
		if searchterms['authors']:
			qcombinations4=(' author:' +  ' ' + y + ' ' + x for y in searchterms['authors'] for x in searchterms['freqwords'][:3])
			genlist.append(qcombinations4)
	else:
		print "Too little information, sorry"
	for x in genlist:
		for i in x:
			d={'dev_key': devkey, 'q': i, 'sort': 'CITED desc', 'fl':'bibcode'}
			response=requests.get( "http://adslabs.org/adsabs/api/search/", params=d)
			results=response.json()
			finalresults.append(results)
	gram=histogrammer(finalresults)
	print "\n\n\nSuggested bibcode: ", gram[0]
	print "All returned bibcodes, sorted by frequency and then date: ", gram



def histogrammer(finalresults):
	fr=str(finalresults)
	bibcode=re.compile(r'\'(\d{4}.*?)\'')
	allbibs=bibcode.findall(fr)
	if allbibs==[]:
		print "\n\n\nI didn't find anything in ADS "
	hg=defaultdict(int)
	for b in allbibs:
		hg[b]+=1
	return sorted(hg.items(), key= lambda x: (x[1], x[0][0:4]), reverse=True)

query_generator(run_program(text))
