#!/usr/bin/python

"""
This is an example of what bad indentation can cause.
In this example it will cause a compliation abort with an IndentationError.

	Mark Veltzer <mark@veltzer.net>
"""
x=6
if x==5:
        print("gdbye")
	 print("hello")
