#!/usr/bin/python

"""
A script to separate the john bryce pdf to separate slides...
"""

import subprocess # for check_output
import os.path # for isfile

subprocess.check_output([
	'pdfseparate',
	'Secure Development - General - 5 days Course.pdf',
	'page-%d.pdf',
])
slide=1
till=166
width=283-90
height=498-340
margin_x=50 # ?!? guessing again
for x in range(1,till):
	filename='page-{x}.pdf'.format(x=x)
	if not os.path.isfile(filename):
		raise ValueError('no such file '+filename)
	slide_name='slide-%03d.pdf' % (slide)
	slide+=1
	start_x=90
	start_y=340
	to_x=start_x+width
	to_y=start_y+height
	frmt='{start_x} {start_y} {to_x} {to_y}'.format(
		start_x=start_x,
		start_y=start_y,
		to_x=to_x,
		to_y=to_y,
	)
	print('frmt is', frmt)
	subprocess.check_output([
		'pdfcrop',
		filename,
		'--bbox',
		frmt,
		slide_name,
	])
	start_x+=width+margin_x
	to_x=start_x+width
	to_y=start_y+height
	slide_name='slide-%03d.pdf' % (slide)
	slide+=1
	frmt='{start_x} {start_y} {to_x} {to_y}'.format(
		start_x=start_x,
		start_y=start_y,
		to_x=to_x,
		to_y=to_y,
	)
	print('frmt is', frmt)
	subprocess.check_output([
		'pdfcrop',
		filename,
		'--bbox',
		frmt,
		slide_name,
	])
	start_x+=width+margin_x
	to_x=start_x+width
	to_y=start_y+height
	slide_name='slide-%03d.pdf' % (slide)
	slide+=1
	frmt='{start_x} {start_y} {to_x} {to_y}'.format(
		start_x=start_x,
		start_y=start_y,
		to_x=to_x,
		to_y=to_y,
	)
	print('frmt is', frmt)
	subprocess.check_output([
		'pdfcrop',
		filename,
		'--bbox',
		frmt,
		slide_name,
	])
