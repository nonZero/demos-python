#!/usr/bin/python

import urllib2
import xml.etree.cElementTree as ET
import csv

def parse_feed(feed):
	rss=ET.fromstring(feed)
	for item in rss.findall('channel/item'):
		date=item.findtext('pubDate').strip()
		package, version=item.findtext('title').split()
		description=item.findtext('description')
		yield (date, package, version, description)

def write_csv(fname, parsed_feed):
	with open(fname,'wb') as f:
		writer=csv.writer(f)
		writer.writerows(parsed_feed)

feed=urllib2.urlopen('http://pypi.python.org/pypi?:action=rss').read()
parsed_feed=parse_feed(feed)
write_csv('pypi.csv', parsed_feed)
