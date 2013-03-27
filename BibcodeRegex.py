import re
import traceback
from collections import defaultdict
import pprint
import bibstemtojournaldict


# Put file info here. 
#Sometimes input journal names will be different from journal names in 
#dictionary and will need to be manually resolved

inputfilename=
outputfilename=

bibcodedict= bibstemtojournaldict.journaldict
reversebibcodedict= dict((name, bib) for bib, name in bibcodedict.items())

file=open(inputfilename, 'r')
records=file.read()
file.close()

records=records.split('\n')
#sometimes there are empty lines, so check for content here
records=[x for x in records if x if '.' in x]


def generatebibcode(altjfield, author):
	#assuming there is 1 and only 1 four digit number that begins with 1 or 2 (ISSN number doesn't count, as it is stripped in first function)
	year=re.search(r'(?:1|2)(?:0|9|8|7)\d\d', altjfield)
	year=year.group()
	#Find journal name--make sure nothing weird in the name (unexpected punctuation, etc) causes this to fail
	j_name= re.search(r'^\s{0,2}([A-Z]+[\w\s.\']*)', altjfield)
	j_name=j_name.group()
	#get rid of extra spaces before, after, or in between words in journal name
	j_name=j_name.strip()
	j_name=j_name.replace('  ', ' ')
	j_name=j_name.replace('   ', ' ')
	j_abbrev=reversebibcodedict[j_name]
	vol=re.search(r'(?:Volume|volume|Vol\.|vol\.|Vol|vol)\s*(\d{1,3})', altjfield)
	vol=vol.group(1)
	if len(vol)==1:
		vol='...'+vol
	elif len(vol)==2:
		vol='..'+vol
	elif len(vol)==3:
		vol='.'+vol
	elif len(vol)==4:
		vol=vol
	page=re.search(r'(?:P.|p.|P|p)\s*(\d{1,3})', altjfield)
	page=page.group(1)
	if len(page)==1:
		page='...'+page
	elif len(page)==2:
		page='..'+page
	elif len(page)==3:
		page='.'+page
	elif len(page)==4:
		page=page
	M='.'
	bibcode=year+j_abbrev+vol+M+page+author
	return bibcode

def export_info_and_errors(finallist, errorlog, file_path=outputfilename):
	print ("\nTotal number of successful output lines is %d.\nTotal number of errors is %d, "
		"with %s distinct error type(s).\n") % (len(finallist), len([x for v in errorlog.values() for x in v]), len(errorlog.keys()))
	counter=1
	if len(errorlog)!=0:
		print "~List of Error Types~"
		for x in errorlog:
			print counter, ":", x
			counter +=1
		print "Full Errorlog: "
		pprint.pprint(errorlog)
	file=open(file_path, 'w')
	file.seek(0)
	file.write('\n'.join(finallist))
	file.close()

def process_two_fielded_entries(list_of_records, file_path):
	finallist=[]
	errorlist=[]
	errorlog={}
	for rec in list_of_records:
		try:
			line=rec
			#use these lines to do any simple string substitutions to clean up the records
			line=line.replace('Pis\'ma', 'Pisma')
			line=re.sub(r'\s{1,2}\(ISSN:?\s* \d{4}-\d{4}\)', '', line)
			#assumes 19 char bibcode at beginning of list
			bib=re.match(r'(\d{4}([\w&]{5}|[\w&]{4}\.|[\w&]{3}\.\.).{10})', line)
			bibcode=bib.group(0)
			author=bibcode[-1]
			j_abbrev=bib.group(2)
			#find full name of journal indicated in bibcode
			firstjname=bibcodedict[j_abbrev]
			justfields=re.sub(r'(\d{4}([\w&]{5}|[\w&]{4}\.|[\w&]{3}\.\.).{10})', '', line)
			# return  main journal field
			#if main journal field is first, it will be preceded by a tab as in the first pattern, and end with a page number followed by first word of alt title.
			#If first journal field ends with "Research supported by" or something, it will be treated as first lines of alt field and will still look good at the end of processing (probably)
			#if it is currently second, it will end with end-of-line as in second pattern.
			firstjfieldfinder=re.search(r'\t.?\(?' + '(?P<field1>' + firstjname + '.*?\d[.]?' +')' + '\)?\s*[A-Z]\w+' + '|' + '\s*' + '(?P<field2>' + firstjname + '[^\n]*?' + ')' + '\r?$', justfields)
			if firstjfieldfinder.group('field1')!=None:
				firstjfield=firstjfieldfinder.group('field1')
			else:
				firstjfield=firstjfieldfinder.group('field2')

			#return journal field that should go second
			altjfield= justfields.replace(firstjfield, '')
			#get rid of parentheses and space characters that might or might not bracket words in the field
			altjfield=re.search(r'^\t?\(?\)?(.*?)\)?\s*\r?$', altjfield)
			try:
				altjfield=altjfield.group(1)
			except AttributeError:
				altjfield=altjfield
			# wrap it in altjournal tags
			#you might not want to match language after the word 'translation'
			#so you can alter the regex on a case-by-case basis
			if re.search(r'Translation', altjfield):
				altjfieldtagged=re.sub(r'^(.*?)(Translation).*$', r'<ALTJOURNAL>\1</ALTJOURNAL> \2', altjfield)
			else:
				altjfieldtagged=re.sub(r'^(.*)$', r' <ALTJOURNAL> \1 </ALTJOURNAL>', altjfield)

			#generate new bibcode
			newbib= generatebibcode(altjfield, author)

			#combine the two journal fields
			newfields= firstjfield+ ' ' + altjfieldtagged

			finalentries= bibcode+ '\t' + newbib+ '\t' + newfields
			finallist[len(finallist):]=[finalentries]
		except Exception, msg:
			tup= (traceback.format_exc(), line)
			errorlist.append(tup)
	errorlog=defaultdict(list)
	for x, y in errorlist:
		errorlog[x].append(y)
	#run output function
	export_info_and_errors(finallist, errorlog)



process_two_fielded_entries(records, outputfilename)