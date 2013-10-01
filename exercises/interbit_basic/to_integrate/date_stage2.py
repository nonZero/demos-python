#!/usr/bin/python

days_in_months=[31,28,31,30,31,30,31,31,30,31,30,31]
days_in_months_leap_year=[31,29,31,30,31,30,31,31,30,31,30,31]
months_names=["January","February","March","April","May","June","July","August","September","October","November","December"]
name_to_days_num={}
for i in range(12):
	name_to_days_num[months_names[i]]=days_in_months[i]

def get_num_of_days_in_month(month_name):
	if (name_to_days_num.has_key(month_name):
		return name_to_days_num[months_name]
	else:
		print "No such month"
def get_following_month(month_name):
	if (name_to_days_num.has_key(month_name):
		i=months_names.index(month_name)
		return months_names[(i+1)%12]
	else:
		print "No such month"
def is_leap_year(year):
		return ((year%4==0) and (year%1000!=0))
class Date:
	def __init__(self, day, month, year):
		if ( (type(day)!=type(1)) or (type(month)!=type(1)) or (type(year)!=type(1))):
			print "Date must be initialized with numbers"
			return
		if ((month<1) or (month>12)):
			print "Month must be between 1 and 12"
			return
		if (is_leap_year(year)):
			if ( (day<0) or (day>days_in_months_leap_year[month-1])):
				print "Day must be between 1 and ", days_in_months[month-1]
				return
		else:
			if ( (day<0) or (day>days_in_months[month-1])):
				print "Day must be between 1 and ", days_in_months[month-1]
				return
		self.day=day
		self.month=month
		self.year=year

	def __gt__(self,other):
		""" Overloading operator>for dates """
		if (self.year>other.year):
			return True
		elif (self.year==other.year):
			if (self.month>other.month):
				return True
			elif (self.month==other.month):
				if(self.day>other.day):
					return True
		return False

	def __lt__(self,other):
		""" Overloading operator<for dates """
		return other>self

	def __eq__(self,other):
		""" Overloading operator==for dates """
		return ( (self.year==other.year) and (self.month==other.month) and (self.day==other.day))

	def __ne__(self,other):
		""" Overloading operator!=for dates """
		return not (self==other)

	def __le__(self,other):
		""" Overloading operator<=for dates """
		return (self<other) or (self==other)

	def __ge__(self,other):
		""" Overloading operator>=for dates """
		return (self>other) or (self==other)

	def __str__(self):
		return str(self.day)+"."+str(self.month)+"."+str(self.year)
