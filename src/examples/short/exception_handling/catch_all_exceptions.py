#!/usr/bin/python2

from __future__ import print_function

'''
Example for catching all exception types.
'''

try:
    raise ValueError('hello')
# this next line catches all exceptions, logs and throws them back...
except Exception as e:
    print('in except', e)
    raise e
finally:
    print('finally is here')
