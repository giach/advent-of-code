from collections import defaultdict

def check_existence(d, s):
	return d[s] == 1


def part1():
	# blocks = [0,2,7,0]
	blocks = [14,0,15,12,11,11,3,5,1,6,8,4,9,1,8,4]
	d = defaultdict(lambda: 0)
	n = len(blocks)
	s = ""
	count = 0
	count2 = 0

	while True:
		max_val = max(blocks)
		max_idx = blocks.index(max_val)

		a = max_val // n
		b = max_val % n

		blocks[max_idx] = 0

		blocks = map(lambda x: x + a, blocks)

		i = max_idx + 1
		i %= n
		while b:
			blocks[i] += 1
			i += 1
			i %= n
			b -= 1

		s = "".join(map(lambda x: str(x), blocks))
		count += 1

		if d[s] == 1:
			break

		d[s] = 1
		if d['141312119886644311012'] == 1:
			count2 += 1



	print(count, count2, s)
part1()