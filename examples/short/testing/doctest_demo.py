#!/usr/bin/python

"""
This is a simple doctest example.

	Mark Veltzer <mark@veltzer.net>
"""
import doctest # for testmod

def triple(x):
	""" return x*3

	>>> triple(7)
	21
	"""
	return x*3

def square(x):
	""" return the square of x

	>>> square(7)
	49
	"""
	# notice this bug...
	return x*x+1

doctest.testmod()
