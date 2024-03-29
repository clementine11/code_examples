# -*- coding: utf-8 -*-

from string import punctuation as punct
import csv


'''This class uses (and slightly expands) Open Refine's 'fingerprint' functionality to merge similar row names in a 
csv file on a per-column basis. 

To use this module:

First create a class by typing classname = Refine(csvfilepath) with the optional additional 
arguments 'dialect', delimiter' and 'lineterminator' to tell Python how to interpret the CSV. You access individual 
columns by using classname.columnname syntax.

NOTE: This module assumes the first row is a row of column names! If you don't have any names, this won't work. 

If you want to standardize a column of names, you can run classname.namefix(classname.columnname) and all 
identical names will be made to have consistent formatting. If you are working  with person names, and set the 
optional parameter lastnamefirst=True, the names will be returned in 'Lastname, First, Middle' format.
If you want to make things even more standardized, you can then run classname.simfind(classname.columnname) to 
have the program suggest words within one letter of similarity. You can either accept or reject these changes. 
Type the name of your class at any time to see what your updated table looks like (Columns will be printed as 
rows for ease of scanning).

 When you are happy with the changes, save them  directly to the file by typing classname.save() '''

class Column(object):
	def __init__(self, columnlist, order):
		self.columnlist=[x.strip() for x in columnlist]
		self.order=order

	def update(self, replacementdict):
		for i, x in enumerate(self.columnlist):
			try:
				self.columnlist[i]=replacementdict[x]
			except KeyError:
				continue
	def __str__(self):
		return str(self.columnlist)
	def __repr__(self):
		return str(self.columnlist)

	def __iter__(self):
		for c in self.columnlist:
			yield c

class Refine(object):

	def __init__(self, csvfile, dialect='excel', delimiter=',', lineterminator = '\r\n'):
		self.csvfile=csvfile
		with open(csvfile, 'rb+') as csvobject:
			creader=csv.reader(csvobject, dialect=dialect, delimiter=delimiter, lineterminator=lineterminator)
			self.delimiter=delimiter
			self.lineterminator=lineterminator
			self.dialect=dialect
			self.clist=[]
			for row in creader:
				self.clist.append(row)
			self.colnames=[x.replace(' ', '_').strip() for x in self.clist[0]]
			list_of_column_objects=[]
			for index, item in enumerate(self.colnames):
				setattr(self, item, Column([x[index] for x in self.clist][1:], index))
				list_of_column_objects.append(item)
			print "\n Welcome to refine.py. Your csv file has been initialized.\n The columns you can access using the instancename.columname syntax are: %s\n" % (str(self.colnames))	


	def __str__(self):
		container=[]
		print "beginning of table"
		for i, x in enumerate(self.colnames):
			y=getattr(self, self.colnames[i])
			print x, ":", y
		return "end of table"

	def __repr__(self):
		container=[]
		print "beginning of table"
		for i, x in enumerate(self.colnames):
			y=getattr(self, self.colnames[i])
			print x, ":", y
		return "end of table"
			

	def namefix(self, colname, lastnamefirst=False):
		keylist=[]
		for d in colname:
			fp=d.strip()
			fp=fp.lower()
			for p in punct:
				fp=fp.replace(p, '')
			fp=fp.split()
			fp.sort()
			fp=' '.join(fp)
			kt=(fp, d)
			keylist.append(kt)
		namedict={}
		for k in keylist:
			namedict.setdefault(k[0], []).append(k[1])
		rd=namedict.items()
		if lastnamefirst==True:
			replacementitems=[]
			for x in namedict.items():
				key=x[1][0].split()
				key=[key[-1]+ ','] + key[:-1]
				key=' '.join(key).title()
				words=[(y, key) for y in x[1]]
				replacementitems.extend(words)
			replacementdict=dict(replacementitems)
			colname.update(replacementdict)
		else:
			replacementitems=[]
			for x in namedict.items():
				key=x[1][0].split()
				key=' '.join(key).title()
				words=[(y, key) for y in x[1]]
				replacementitems.extend(words)
			replacementdict=dict(replacementitems)
			colname.update(replacementdict)
		
	def simfind(self, colname):
		keylist=[]
		for d in colname:
			fp=d.strip()
			fp=fp.lower()
			for p in punct:
				fp=fp.replace(p, '')
			fp=fp.split()
			fp.sort()
			fp=' '.join(fp)
			kt=(fp, d)
			keylist.append(kt)
		namedict={}
		for k in keylist:
			namedict.setdefault(k[1], []).append(k[0])
		for k in namedict.keys():
			namedict[k]=list(set(namedict[k]))[0]
		reversenamedict=dict(zip(namedict.values(), namedict.keys()))
		for key1 in namedict.values():
			for key2 in namedict.values():
				x=(key1, key1.replace(' ',''))
				y=(key2, key2.replace(' ',''))
				d=len(x[1])-len(y[1])
				if d== 1:
					diffcount=0
					adjustment=0
					for i in range(len(y[1])):
						if x[1][i]==y[1][i+adjustment]:
							continue
						else:
							diffcount+=1
							adjustment-=1
							if diffcount>1:
								break
					if x[1][-1]!=y[1][-1]:
						diffcount+=1	
					if diffcount==0:
						diffcount=1	
					if diffcount==1:
						print "If you agree, I will merge the following: ", reversenamedict[x[0]], 'and ', reversenamedict[y[0]]
						ri=raw_input("Type 'y' to agree, 'n' to disagree: ")
						if ri=='y' or ri=='Y':
							i=raw_input('Which name should be the one that is kept? Type 1 to keep the first name, or 2 to keep the second: ')
							if '1' in i:
								replacementdict=dict([(reversenamedict[y[0]], reversenamedict[x[0]])])
								colname.update(replacementdict)
							elif '2' in i:
								replacementdict=dict([(reversenamedict[x[0]], reversenamedict[y[0]])])
								colname.update(replacementdict)

	def save(self):
		with open(self.csvfile, 'wb') as newcsv:
			newwriter=csv.writer(newcsv, dialect=self.dialect, delimiter=self.delimiter, lineterminator = self.lineterminator,  quoting=csv.QUOTE_MINIMAL)
			columns=[]
			newwriter.writerow([x.replace('_', ' ') for x in self.colnames])
			for i, x in enumerate(self.colnames):
				i= getattr(self, x)
				columns.append(list(i))
			for i in range(len(columns[0])):
				row=[x[i] for x in columns]
			for x in row:
				newwriter.writerow(row)

