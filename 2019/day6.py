from collections import defaultdict
from collections import Counter

def read_file():
	lines = []
	with open("day_6_input") as fp:
		line = fp.readline().rstrip()

		while line:
			lines += [line.split(")")]
			line = fp.readline().rstrip()


	return lines

def part1():
	d = defaultdict(lambda: [])
	dd = defaultdict(lambda: [])
	lines = read_file()

	for t in lines:
		d[t[0]] += [t[1]]


	queue = []
	key = 'VM4'
	values = d[key]
	d[key] = []
	while True:
		for e in values:
			dd[key] += ()

part1()
