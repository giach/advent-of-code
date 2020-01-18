# Part 1

def read_file():
	with open('day_5_input') as fp:
		line = fp.readline()

	# to_int = lambda x: int(x, 10)
	# instr = map(to_int, line.split(','))
	instr = line.split(',')
	return instr

def increm_pointer(opcode):
	if opcode == 1:
		return 4
	if opcode == 2:
		return 4
	if opcode == 3:
		return 3
	if opcode == 4:
		return 3

def decode_arthm_instr(instr):
	opcodes = ["01", "02"]
	op = instr[-2:]
	if op not in opcodes:
		return (None, [])
	pad = 5 - len(instr)
	instr = "0" * pad + instr
	op = int(op, 10)
	params = instr[:-2]
	params = map(lambda x:int(x, 10), params)

	return (op, params)

def decode_io_instr(op):
	opcodes = ["3","4"]
	if op not in opcodes:
		return (None, [])
	return (op, [])

def decode_instr(instr):
	(opcode, parms) = decode_arthm_instr(instr)
	if not opcode :
		(opcode, parms) = decode_io_instr(instr)

	if opcode:
		return (opcode, parms)
	else:
		return (None, [])

def compute(instrs):
	i = 0
	print(instrs)

	(opcode, parms) = decode_instr("11101")
	print(parms)
	op1 = instrs[instrs[i+1]] if parms[-1] == 0 else instrs[i+1]
	op2 = instrs[instrs[i+2]] if parms[-2] == 0 else instrs[i+2]
	op3 = instrs[instrs[i+3]] if parms[-3] == 0 else instrs[i+3]

	print(op1,op2,op3)

	# while opcode:
	# 	(opcode, parms) = decode_instr(instr[i])

	# 	if opcode == 1:
	# 		op1 = instr[instr[i+1]] if parms[-1] == 0 else instr[i+1]
	# 		op2 = instr[instr[i+2]] if parms[-2] == 0 else instr[i+2]
	# 		op3 = instr[instr[i+3]] if parms[-3] == 0 else instr[i+3]


	# 		instr[op3] = instr[op1] + instr[op2]
	# 	if opcode == 2:
	# 		instr[instr[i+3]] = instr[instr[i+1]] * instr[instr[i+2]]
	# 	if opcode == 99:
	# 		break
	# 	i += increm_pointer(instr[i])
	# return instr

instructions = read_file()
compute(instructions)