#!/usr/bin/python2

'''
This example explores how python allocates memory.
This example assumes that you are watching the memory
utilisation of this program from outside using the OS or something.

TODO:
- make this program output it's own memory utilisation via OS mechanisms.
- show pythons APIs for knowing how much RAM you are wasting.
- compare the two and discuss the conclusions.
'''

import time

acc = []
counter = 0
while True:
    print('counter is ' + str(counter))
    counter += 1
    l = []
    l = range(0, 1024)
    acc.append(l)
    time.sleep(2)
