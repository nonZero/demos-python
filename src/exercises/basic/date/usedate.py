#!/usr/bin/python3

import date

baddate1 = date.Date(37, 4, 5)
baddate2 = date.Date(-5, 4, 5)
baddate3 = date.Date(12, -1, 5)
baddate4 = date.Date(12, 13, 5)
d1 = date.Date(26, 2, 84)
d2 = date.Date(12, 1, 88)

print(d1 > d2)
print(d1 < d2)

print(d1)
print(d2)
