#!/usr/bin/python

"""
A demo of sets

	Mark Veltzer <mark@veltzer.net>
"""

# create an empty set
a=set()
# add elements
a.add("mark");
a.add("doron");
# print the set
print a
# check whether an element is in the set
print "mark" in a
print "shay" in a
# iterate the set
for x in a:
	print x
# remove an element
a.remove("mark")
print a
try:
	a.remove("shay")
except:
	print "yes, getting exceptions for removing elements not from the set"
