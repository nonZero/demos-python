#!/usr/bin/python

f=open('c:/tmp.txt')
report={}
lines=f.readlines()
for line in lines:
	for c in line:
		if not(c in [' ','\n','\r','\t']):
			if c in report:
				report[c]+=1
			else:
				report[c]=1
f=open('c:/tmp2.txt','wa')
for c in report.keys():
	f.write(c)
	f.write(' : ')
	f.write(str(report[c]))
	f.write('\n')
f.close()
