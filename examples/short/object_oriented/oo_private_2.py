#!/usr/bin/python

'''
This example shows that private values (values stored in attributes
whose names is prefixed by one or two underscores) are not really private.
- _values can be changed as is.
- __values are just hidden in funny names. The reason for this is ofcourse inheritance.

NOTE: new style (deriving from 'object') type object or old style object make no
difference as to this point.
'''

from __future__ import print_function

class Book(object):
	def __init__(self,price,name):
		self.__price=price
		self._name=name
	def printMe(self):
		print('price is',self.__price)
		print('name is',self._name)
	def setPrice(self,price):
		self.__price=price
	def getPrice(self):
		return self.__price
	def setName(self,name):
		self._name=name
	def getName(self):
		return self._name

b=Book(50,'Lord of the Rings')
b.printMe()
# lets try to change the __price attribute directly...
# Notice that we get an exception not because the attribute is 'private'
# but rather because such an attribute really DOES NOT exist...
try:
	print('price is',b.__price)
except AttributeError as e:
	print(e)
	print('You see,you cannot directly change the attribute because THERE IS no such attribute')
# We CAN change the name since attributes that have just one _ in front of them appear AS IS
# in the object
print('if you see silmarilion below it means we changed the attribute even though it has _ in front of it')
b._name='silmarilion'
b.printMe()

# Now lets see what the object really has...
print(dir(b))

# OK. I got it,the object really has the '_Book__price' attribute. Lets see if we can change
# that... YES WE CAN...
print('if you see price=70 it means we changed the attribute even though it has __ in front of it')
b._Book__price=70
b.printMe()
