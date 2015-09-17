#!/usr/bin/python3


def single_min_max_sum(x, y):
    if x < y:
        min = x
        max = y
    else:
        min = y
        max = x
    sum = x + y
    return [min, max, sum]


def min_max_avg(list):
    tup = reduce(single_min_max_sum, list)
    return tup[0], tup[1], tup[2] / len(list)

print(min_max_avg(xrange(0, 100000)))
