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
