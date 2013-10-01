#!/usr/bin/python

"""
Example of sorting with python.
Notice the passing of the comparator and it's triped (1,0,-1) return value.

	Mark Veltzer <mark@veltzer.net>
"""
def compare(a,b):
	if a[1]<b[1]:
		return -1
	if a[1]==b[1]:
		return 0
	if a[1]>b[1]:
		return 1

m={ "mark": 10,"yossi": 3,"doron": 67 }
arr=m.items()
arr.sort(cmp=compare)

for x in arr:
	print(arr[0]+" "+str(arr[1]))
