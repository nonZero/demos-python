#!/usr/bin/python2

'''
An example demonstrating twisteds 'callInThread' function.
'''

from twisted.internet import reactor
import time  # for sleep


def aSillyBlockingMethod(t, stop):
    print('starting...')
    time.sleep(t)
    print(t, 'seconds have passed')
    # this will not work as we are running in a separate thread...
    # if stop:
    #	reactor.stop()
    # instead we must do:
    if stop:
        reactor.callFromThread(reactor.stop)

# run method in thread
reactor.callInThread(aSillyBlockingMethod, 10, True)
reactor.callInThread(aSillyBlockingMethod, 5, False)
print('before suggestThreadPoolSize')
reactor.suggestThreadPoolSize(2)
time.sleep(10)
print('finished sleeping...')
reactor.run()
