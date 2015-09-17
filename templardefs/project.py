'''
project definitions for templar
'''

def populate(d):
	d.project_name='demos-python'
	d.project_long_description='Demos for the Python programming language'
	d.project_year_started='2010'
	d.project_description='''This project explores the python programming language.
The idea is that when you are programming you may find many examples
over the Internet but you always need to tweek them a bit to see
how you can get to an example which answers your needs precisely.
Over the Internet this is hard to do. But if you clone hundreds
of examples and you have them in working condition on your machine
you can just find the example which is closest to what you need
and tweek it until it does exactly what you need. You may even
add your example as a new example or contribute it back to this project.
This is a much better way of programming since you are not doing
the experiments on your full system but rather on a small example
that is easy to run, debug and manage. Once you have the example ready and
running correctly you can incorporate it's code into a larger project.'''.format(**d)

def getdeps():
	return [
		__file__, # myself
	]
