#!/usr/bin/python3

def min_max_avg(list):
	min=list[0]
	max=list[0]
	sum=list[0]
	for x in list[1:]:
		if x<min:
			min=x
		if x>max:
			max=x
		sum+=x
	return (min,max,sum/len(list))

print(min_max_avg(xrange(0,100000)))
