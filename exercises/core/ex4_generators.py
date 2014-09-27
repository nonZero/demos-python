#!/usr/bin/python3

import textwrap

def lines2paragraphs(lines):
	'''Group lines into paragraphs: as lists of lines.'''
	paragraph=[]
	for line in lines:
		if not line.strip():
			yield paragraph
			paragraph=[]
		else:
			paragraph.append(line)
	# The last paragraph remains
	# (if the input didn't end with an empty line)
	if paragraph:
		yield paragraph

def reformat(lines):
	'''Generate lines of reformatted paragraphs.

	Paragraph in input and output are separated by empty lines.
	'''
	for p in lines2paragraphs(lines):
		for line in textwrap.wrap('\n'.join(p)):
			yield line
		yield ''

if __name__=='__main__':
	print(list(reformat(['foo', 'bar', 'baz', '', 'quux', 'quuux'])))
