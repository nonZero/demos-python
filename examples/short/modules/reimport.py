#!/usr/bin/python

'''
Show how to import different modules and treat them as the same one.
'''

from __future__ import print_function
import imp

import reimport_one
print('add(2,2) is',reimport_one.add(2,2))
import reimport_two as reimport_one
print('add(2,2) is',reimport_one.add(2,2))
