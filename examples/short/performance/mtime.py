#!/usr/bin/python3

'''
This example explores whether it is efficient or not to cache os.path.getmtime()
data in user space in python.

You can see that os.path.getmtime() in python is *always* a syscall by doing
something like:
	strace ./mtime.py 2>&1 > /dev/null | grep stat64 | grep etc | wc
when running this.

The answer is: YES!!!
'''

import time  # for time
import random  # for ???
import os  # for unlink
import os.path  # for isfile, getmtime
import glob  # for glob

#
# parameters #
#
count = 1000000
doFirst = True
doSecond = True

#
# code #
#

# get the list of all files accessible from /etc
files = [f for f in glob.glob('/etc/*') if os.path.isfile(f)]
files.extend([f for f in glob.glob('/etc/*/*') if os.path.isfile(f)])
listlen = len(files)
print('file list length is {listlen}...'.format(listlen=listlen))

# now do lots of os.path.getmtime() ops on them
if doFirst == True:
    time_before = time.time()
    for i in range(count):
        filename = files[i % listlen]
        os.path.getmtime(filename)
    time_after = time.time()
    print('time taken for {count} os.path.getmtime : {time:.3f} seconds'.format(
        time=time_after - time_before,
            count=count,
    ))

if doSecond == True:
    # now do the same with a cache
    times = dict()
    time_before = time.time()
    for i in range(count):
        filename = files[i % listlen]
    if filename in times:
        t = times[filename]
    else:
        times[filename] = os.path.getmtime(filename)
    time_after = time.time()
    print('time taken for {count} cache getmtime : {time:.3f} seconds'.format(
        time=time_after - time_before,
            count=count,
    ))
