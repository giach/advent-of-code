def part1():
	fuel = 0
	with open('day_1_input_1') as fp:
		line = fp.readline()
		while line:
			mass = int(line, 10)
			fuel += (mass // 3 - 2)
			line = fp.readline()

	return fuel


print(part1())

def get_module_fuel(n):
	fuel = 0
	while (n // 3 - 2) > 0:
		new_fuel = (n // 3 - 2)
		fuel += new_fuel
		n = new_fuel
	return fuel

def part2():
	fuel = 0

	with open('day_1_input_2') as fp:
		line = fp.readline()
		while line:
			fuel += get_module_fuel(int(line, 10))
			line = fp.readline()
	return fuel

print(part2())

print(get_module_fuel(1969))