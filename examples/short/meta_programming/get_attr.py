#!/usr/bin/python2

'''
This is an example of overloading the __getattr__ python method. This allows
one to pretend to have various attributes or to decide that attributes
come in and out of scope at runtime. Uses for this could include:
- testing and simulation of errors.
- Aspect Oriented Programming.
- Proxy implementations.
- ORM solutions.
- Backwards compatibility solutions.
And more...
'''


class A(object):

    def __init__(self):
        pass
        # self.d={}

    def __getattr__(self, name):
        return name[::-1]
        # def mymethod(self):
        #	print('in here with name',name)
        # return mymethod

    def __setattr__(self, name, val):
        # print('ERROR! don't touch this...')
        # getattr(self,'d').__setitem__('\''+name+'\'',val)
        pass


a = A()
print(dir(a))
print(a.whatIsThis)
print(a.whatsGoingOn)
print(a.howManyAttributesDoesThisObjectHave)
# a.myprivate=7
