#!/usr/bin/python2

'''
this is an example of building your own iterator
In this example the object returns itself as the iterator
(the return value from the __iter__ function). But it could have
chosen to return another object.
'''

'''Iterator for looping over a sequence backwards'''
class Reverse:
	def __init__(self,data):
		self.data=data
		self.index=len(data)
	def __iter__(self):
		return self
	def next(self):
		if self.index==0:
			raise StopIteration
		self.index=self.index-1
		return self.data[self.index]

'''
And now lets use the iterator...
'''
l=[1,2,3,4,5,6,7]
for x in Reverse(l):
	print(x)
