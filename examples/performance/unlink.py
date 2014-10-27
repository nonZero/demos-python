#!/usr/bin/python3

'''
this example explores whether it is better to not remove files vs the try/except
paradigm or rather via the os.path.isfile paradigm.

it proves that maintaining a cache in user space is the best approach.
'''

import time # for time
import os # for unlink
import os.path # for isfile

count=1000000
time_before=time.time()
for i in range(count):
	filename='unknown'+str(i%1000)+'.nosuchending'
	try:
		os.unlink(filename)
	except:
		pass
time_after=time.time()
print('time taken for {count} os.unlinks + exception handling : {time:.3f} seconds'.format(
	time=time_after-time_before,
	count=count,
))

time_before=time.time()
for i in range(count):
	filename='unknown'+str(i%1000)+'.nosuchending'
	if os.path.isfile(filename):
		os.unlink(filename)
time_after=time.time()
print('time taken for {count} isfile + unlink : {time:.3f} seconds'.format(
	time=time_after-time_before,
	count=count,
))

time_before=time.time()
files=dict()
for i in range(count):
	filename='unknown'+str(i%1000)+'.nosuchending'
	if filename not in files:
		if os.path.isfile(filename):
			os.unlink(filename)
			files[filename]=False
		else:
			files[filename]=False
	else:
		if files[filename]==True:
			os.unlink(filename)
			files[filename]=False
		else:
			pass
time_after=time.time()
print('time taken for {count} cached unlink ops : {time:.3f} seconds'.format(
	time=time_after-time_before,
	count=count,
))
