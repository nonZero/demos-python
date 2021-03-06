#!/usr/bin/python3

'''
This is an example of the 'os.walk' API that allows one to traverse
a directory of files recursivly.
This is used to implement find(1)+grep(1) in just a few lines of python.
'''

import os  # for walk
import re  # for compile, finditer
import sys  # for argv
import os.path  # for join

if len(sys.argv) < 2:
    raise ValueError('please pass regexp')
c = re.compile(sys.argv[1])

for root, dirs, files in os.walk('.'):
    for file in files:
        full = os.path.join(root, file)
        for num, line in enumerate(open(full)):
            # remove the new line
            line = line[:-1]
            for x in c.finditer(line):
                print('{0},{1}: {2}'.format(full, num, line))
