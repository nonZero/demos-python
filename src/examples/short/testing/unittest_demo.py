#!/usr/bin/python2

'''
This example demonstrates the use of the 'unittest' module.
'''

import unittest  # for TestCase, main


class myunittest(unittest.TestCase):

    def testThis(self):
        sum = 0
        for x in xrange(0, 100):
            sum += x
        self.assert_(sum == 4950)

unittest.main()
