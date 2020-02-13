from collections import defaultdict

def read_file():
	points = []
	y = 0
	with open("day10_input") as fp:
		fline = fp.readline()
		while fline:
			line = list(fline)[:-1]
			xs = [i for i, elem in enumerate(line) if elem == '#']
			points += [(x,y) for x in xs]
			fline = fp.readline()
			y += 1

	return points

# the matrix will always be (3,3)
def matrix_det(m):
	d1 = m[0][0] * m[1][1] * m[2][2]
	d2 = m[1][0] * m[2][1] * m[0][2]
	d3 = m[2][0] * m[0][1] * m[1][2]

	d4 = m[0][2] * m[1][1] * m[2][0]
	d5 = m[1][2] * m[2][1] * m[0][0]
	d6 = m[2][2] * m[0][1] * m[1][0]

	return d1 + d2 + d3 - d4 - d5 - d6

# (386, (20, 19), 284)
def part1():
	ps = read_file()
	n = len(ps)

	d = defaultdict(list)

	for p1 in ps:
		tmp = set()
		copy1_ps = list(ps)
		copy1_ps.remove(p1)

		for p2 in copy1_ps:
			flag = 0
			copy2_ps = list(copy1_ps)
			copy2_ps.remove(p2)

			for p3 in copy2_ps:
				m = [[p1[0], p1[1], 1], [p2[0], p2[1], 1], [p3[0], p3[1], 1]]

				if matrix_det(m) == 0:
					if p1 > p2:
						t = min(p1,p2,p3)
					if p1 < p2:
						t = max(p1,p2,p3)
					# the current point is in the middle, thus skip it
					if (p1 > p2 and p1 < p3) or (p1 > p3 and p1 < p2):
						continue
					tmp.add(t)

		d[p1] = list(tmp)

	ast  = min(d.items(), key=lambda e: len(e[1]))
	# print(n - 1 - len(ast[1]), ast)


def direct_line_ast(copy1_ps, p1):
	tmp = set()
	for p2 in copy1_ps:
		copy2_ps = list(copy1_ps)
		copy2_ps.remove(p2)

		for p3 in copy2_ps:
			m = [[p1[0], p1[1], 1], [p2[0], p2[1], 1], [p3[0], p3[1], 1]]

			t = (0,0)
			if matrix_det(m) == 0:
				if p1 > p2:
					t = min(p1,p2,p3)
				if p1 < p2:
					t = max(p1,p2,p3)
				# the current point is in the middle, thus skip it
				if (p1 > p2 and p1 < p3) or (p1 > p3 and p1 < p2):
					continue
				tmp.add(t)

	return list(set(copy1_ps) - tmp)

def get_second(near_ast, best_ast):
	cadran1 = sorted([(x,y) for x, y in near_ast if x >= best_ast[0] and y <= best_ast[1]])
	cadran2 = sorted([(x,y) for x, y in near_ast if x > best_ast[0] and y > best_ast[1]])

	return cadran1 + cadran2

def get_first(near_ast, best_ast):
	cadran3 = sorted([(x,y) for x, y in near_ast if x <= best_ast[0] and y > best_ast[1]])
	cadran4 = sorted([(x,y) for x, y in near_ast if x < best_ast[0] and y <= best_ast[1]])

	return cadran3 + cadran4

def panta_dreptei(p1, p2):
	if p1[0] - p2[0] != 0:
		return (p1[1] - p2[1]) / float(p1[0] - p2[0]), p2
	else:
		return -9999, p2


def get_result(ps, best_ast):
	all_points = list(ps)
	all_points.remove(best_ast)

	count = 1
	while True:
		near_ast = direct_line_ast(all_points, best_ast)

		points_second = get_second(near_ast,best_ast)
		points_first = get_first(near_ast, best_ast)

		slopes_second = [panta_dreptei(best_ast, p) for p in points_second]
		slopes_first = [panta_dreptei(best_ast, p) for p in points_first]
		slopes_second = sorted(slopes_second, key=lambda x: x[0])
		slopes_first = sorted(slopes_first, key=lambda x: x[0])

		slopes = slopes_second + slopes_first
		for v, p in slopes:
			all_points.remove(p)

			if count == 200:
				print("g, ", count, p)
				return
			count += 1


def nearby_asts():
	ps = read_file()
	n = len(ps)

	d = defaultdict(list)

	for p1 in ps:
		tmp = set()
		copy1_ps = list(ps)
		copy1_ps.remove(p1)

		d[p1] = direct_line_ast(copy1_ps, p1)

	ast  = max(d.items(), key=lambda e: len(e[1]))

	best_ast = ast[0]
	near_ast = ast[1]
	# print(best_ast, near_ast)

	r = get_result(ps, best_ast)


# ('g, ', 200, (4, 4))
def part2():
	nearby_asts()


# part1()
part2()