#!/usr/bin/python

# We represent directions by (dx, dy), so that updating (x, y) will be
# a matter of simple addition.

emiter2dxdy={'>': (1, 0), '<': (-1, 0), 'v': (0, 1), '^': (0, -1)}

def find_emitter(room):
	"""Return (x, y, dx, dy)"""
	for y, line in enumerate(room):
		for x, char in enumerate(line):
			if char in emiter2dxdy:
				dx, dy=emiter2dxdy[char]
				return x, y, dx, dy

def lasers(fname):
	room=open(fname).readlines()

	x, y, dx, dy=find_emitter(room)

	while True:
		x += dx
		y += dy
		char=room[y][x]

		# uncomment to display path:
		##print x, y, char

		passage={' ': (dx, dy), # continue straight
			'\\': (dy, dx), # flip around dx=dy
			'/': (-dy, -dx)} # opposite result from \
		if char in passage:
			# still going
			dx,dy=passage[char]
		else:
			# hit something
			return char=='x'

for fname in ['lasers_hit.txt', 'lasers_miss.txt']:
	print open(fname).read()
	print lasers(fname)
	print
