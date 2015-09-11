#!/usr/bin/python3

'''
Usage: hangman.py <secret_word>
'''

from ex10_ex11_classes import Hangman

import sys

args=sys.argv[1:]
if len(args)!=1:
	print(__doc__) # usage message
	sys.exit(2)

print('Type 'exit' to exit.')
h=Hangman(args[0])
while True:
	line=raw_input('TYPE A LETTER: ')
	if line.strip().lower() in ['exit', 'quit']:
		break
	h.guess(line)
