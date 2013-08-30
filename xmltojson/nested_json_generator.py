# -*- coding: utf-8 -*-

from lxml import etree 
from collections import defaultdict
from unidecode import unidecode
import re
from sample_word_freq_dict import sample_dict
import os

filepath=os.getcwd()
print filepath+'/astronomy_thesaurus.txt'
xml=open(filepath+'/astronomy_thesaurus.txt')
xmlstuff=xml.read()

xmlstuff=xmlstuff.lower()

xmlstuff=re.sub(r'(\w)(?:-|–|,|\')(\w)', r'\1 \2', xmlstuff)

xmlstuff=xmlstuff.decode('utf-8')
xmlstuff=unidecode(xmlstuff)
termsdict=defaultdict(list)

x=etree.fromstring('<?xml version="1.0" encoding="UTF-8"?>'+xmlstuff)
words=x.xpath('//terminfo')

final_children=[]
all_recs=[]
middle_layers=[]
for w in words:
	main_word=w.xpath('./t/text()')[0]
	children=w.xpath('.//nt/text()')
	parent=w.xpath('.//bt/text()')
	#using dictionary generated elsewhere to append size info
	try:
		size=sample_dict[main_word]
	except KeyError:
		size=0
	#finding final children
	if children==[]:
		num=len(parent)
		a=dict([('name', main_word), ('size', size), ('parent', parent), ('num', num)])
		all_recs.append(a)
		final_children.append(a)
	#these have children (might not have parents though)
	else:	
		num=len(parent)
		a=dict([('name', main_word), ('children', children), ('parent', parent), ('num', num)])
		all_recs.append(a)
		middle_layers.append(a)

#appending final children to their parents
#now one level of nesting
for i, x in enumerate(middle_layers):
	for ii, y in enumerate(x['children']):
		for iii, child in enumerate(final_children):
			if final_children[iii]['num']==0:
				continue
			if y==child['name']:
				middle_layers[i]['children'][ii]=dict([('name', child['name']), ('size', child['size'])])
				final_children[iii]['num']-=1

slated_for_removal=[]

#any child that is not a dictionary needs to be nested
for i, x in enumerate(middle_layers[:]):
	for ii, y in enumerate(x['children']):
		for item in middle_layers[:]:
			#match means y isnt a dict
			if item['name']== y:
			#now, before you transfer the dictionary for the word, test to see if children are only dicts 
			# if not, break, because this node is not ready to be nested
				for c in item['children']:
					if isinstance(c, str):
						break
				middle_layers[i]['children'][ii]=dict([('name', item['name']), ('children', item['children'])])
				slated_for_removal.append(item)

#this should remove anything other than top-level nodes and their nested children
for x in middle_layers[:]:
	if x in slated_for_removal:
		middle_layers.remove(x)


valid_json= str(middle_layers).replace('\'', '\"')
valid_json='{"name": "ADS Astronomical Terms", "children": '+valid_json+ '}'
print valid_json