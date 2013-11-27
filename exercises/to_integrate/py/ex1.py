#!/usr/bin/python

found=True
while found:
	input_string=raw_input("Please give me some digits... \n")
	found=False
	for character in input_string:
		if ord(character)<ord('0') or ord(character)>ord('9'):
			# we have a non digit!
			print "Error, you gave me non digits"
			found=True
			break
print "starting real work on",input_string
# this is the easy solution...
#for digit in range(10):
#	print "digit",digit," appears",input_string.count(str(digit))," times"
# this is the right one...
counters=[0]*10
for digit in input_string:
	counters[int(digit)]+=1
for digit,count in enumerate(counters):
	print "digit",digit," appears",count," times"
