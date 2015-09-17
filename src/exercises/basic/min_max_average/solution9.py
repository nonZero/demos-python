#!/usr/bin/python3

'''
this solution is without the varargs type.
notice that this does prevent us from calling it with the xrange
generator...
also notice the 'import division' to make sure that the division to
calculate the average is done in float.
'''

from __future__ import division


def min_max_avg(num_list):
    '''return a tuple containing the maximnum_list, minimum and avrage of the given num_listbrs'''
    return min(num_list), max(num_list), sum(num_list) / len(num_list)

print(min_max_avg(xrange(100000)))
