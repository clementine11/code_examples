#-*- coding: utf-8 -*-

def make_nltk_freqdist(file):
	import codecs
	#so you can work in unicode
	text=codecs.open(file, encoding='utf-8')
	text=text.read()
	import nltk
	from nltk.corpus import stopwords
	tokens=nltk.word_tokenize(text)
	tokens1=[t.lower() for t in tokens if t.isalpha()]
	stopwords=stopwords.words('english')
	tokens2=[t for t in tokens1 if t not in stopwords]
	tokens3=[t for t in tokens2 if len(t)>1]
	finaltext=nltk.Text(tokens3)
	freqdist=nltk.FreqDist(finaltext)
	print freqdist.keys()[:50]
	freqdist.plot(50, cumulative=True)
	return freqdist




def make_nltk_text(file):
	import codecs
	text=codecs.open(file, encoding='utf-8')
	#so you can work in unicode
	text=text.read()
	import nltk
	tokens=nltk.word_tokenize(text)
	finaltext=nltk.Text(tokens)
	return finaltext


make_nltk_text('/Users/alex/desktop/307merged.txt')
