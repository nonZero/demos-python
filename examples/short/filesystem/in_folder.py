#!/usr/bin/python3

'''
This example shows how to find if a file is in a certain folder.
'''

import sys  # for stdin

for line in sys.stdin:
    (file1, file2) = line.strip().split()
    print(file1.startswith(file2))
