# Part 1

def read_file():
	with open('day_2_input_1') as fp:
		line = fp.readline()

	to_int = lambda x: int(x, 10)
	instr = map(to_int, line.split(','))

	return instr

def compute(instr):
	i = 0

	while True:
		if instr[i] == 1:
			instr[instr[i+3]] = instr[instr[i+1]] + instr[instr[i+2]]
		if instr[i] == 2:
			instr[instr[i+3]] = instr[instr[i+1]] * instr[instr[i+2]]
		if instr[i] == 99:
			break
		i += 4
	return instr

instructions = read_file()
instructions[1] = 12
instructions[2] = 2
print(compute(instructions))

# Part 2 : 19690720

def find_noun_verb():
	for i in range(0,100):
		for j in range(0,100):
			instr = read_file()
			instr[1], instr[2] = i, j

			r =  compute(instr)
			if r[0] == 19690720:
				return i * 100 + j


print(find_noun_verb())