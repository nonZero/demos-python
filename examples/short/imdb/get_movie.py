#!/usr/bin/env python
"""
get_movie.py

Usage: get_movie "movieID"

Show some info about the movie with the given movieID (e.g. '0133093'
for "The Matrix", using 'http' or 'mobile').
Notice that movieID, using 'sql', are not the same IDs used on the web.
"""

import sys
import imdb
import random

if len(sys.argv) != 2:
	print 'Only one argument is required:'
	print ' %s "movieID"' % sys.argv[0]
	sys.exit(2)

movieID = sys.argv[1]

i = imdb.IMDb()

out_encoding = sys.stdout.encoding or sys.getdefaultencoding()

try:
	# Get a Movie object with the data about the movie identified by
	# the given movieID.
	movie = i.get_movie(movieID)
except imdb.IMDbError, e:
	print "Probably you're not connected to Internet.  Complete error report:"
	print e
	sys.exit(3)


print movie.summary().encode(out_encoding, 'replace')
print movie.summary()

for k in movie.keys():
	print k, movie[k]

print '==== "%s" / movieID: %s ====' % (movie['title'], movieID)
imdbURL = i.get_imdbURL(movie)
if imdbURL:
	print 'IMDb URL: %s' % imdbURL
genres = movie.get('genres')
if genres:
	print 'Genres: %s' % ' '.join(genres)
cast = movie.get('cast')
if cast:
	print 'Cast: '
	cast = cast[:5]
	for name in cast:
		print '      %s (%s)' % (name['name'], name.currentRole)
rating = movie.get('rating')
if rating:
	print 'Rating: %s' % rating
i.update(movie, info=['trivia'])
trivia = movie.get('trivia')
if trivia:
	rand_trivia = trivia[random.randrange(len(trivia))]
	print 'Random trivia: %s' % rand_trivia

info_runtime = movie.get('runtime')
print 'Runtime is: {info_runtime}'.format(info_runtime=info_runtime)

info_directors = movie.get('director')
for n,d in enumerate(info_directors):
	#print dir(d)
	print '{n}, {d}'.format(n=n, d=d['name'])
