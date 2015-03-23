#!/usr/bin/python3

'''
This is an example of how to read XML in python using the built in
xml.etree module

'''

import xml.etree.ElementTree # for parse

# both of these will work
mydoc=xml.etree.ElementTree.ElementTree(file='data.xml')
#mydoc=xml.etree.ElementTree.parse('data.xml')
for e in mydoc.findall('.//bar'):
	print(e.get('title'))
