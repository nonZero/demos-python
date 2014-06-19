#!/usr/bin/python

"""
This method shows the types of regular methods vs the types of real static methods.

    Mark Veltzer <mark@veltzer.net>
"""


class Book():
    num = 0

    def __init__(self, price):
        self.__price = price
        Book.num += 1

    def printit(self):
        print('price is', self.__price)

    def setPrice(self, newprice):
        self.__price = newprice

    def getNumBooks():
        return Book.num

    getNumBooks = staticmethod(getNumBooks)

    def getNumBooks2():
        return Book.num

    getNumBooks2 = classmethod(getNumBooks2)


b = Book(15)
print(b.printit, type(b.printit))
print(Book.printit, type(Book.printit))
print(Book.getNumBooks, type(Book.getNumBooks))
print(Book.getNumBooks2, type(Book.getNumBooks2))
