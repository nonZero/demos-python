#!/usr/bin/python3

'''
This is a solution using a dictionary
'''

d = {}
for i in xrange(10):
    d[i] = 0

s = raw_input('Please enter a line of digits: ')
for c in s:
    if c.isdigit():
        d[int(c)] += 1
    else:
        print('you moron')

for i in xrange(10):
    print('{i} appeared {count} times in the text'.format(
        i=i,
            count=d[i]
    ))
