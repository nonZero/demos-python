#!/usr/bin/python2

from __future__ import print_function
import sys # for stdin

last=None
count=0
for line in sys.stdin:
	line=line.rstrip()
	if line==last:
		count+=1
	else:
		if last is not None:
			print(last,count)
		last=line
		count=1
