# Part 1

def read_file():
        with open('day_5_input') as fp:
                line = fp.readline()

        instr = line.split(',')
        return instr

def increm_pointer(opcode):
        if opcode == 1:
                return 4
        if opcode == 2:
                return 4
        if opcode == 3:
                return 2
        if opcode == 4:
                return 2

def decode_arthm_instr(instr):
        opcodes = ["01", "02"]
        op = instr[-2:]
        if op not in opcodes:
                return (None, "arth", [])
        pad = 5 - len(instr)
        instr = "0" * pad + instr
        op = int(op, 10)
        params = instr[:-2]
        params = map(lambda x:int(x, 10), params)

        return (op, "arth", params)

def decode_io_instr(instr):
        opcodes = ["3","4"]
        if instr not in opcodes:
                return (None, "io", [])
        return (instr, "io", [])

def decode_instr(instr):
        (opcode, optype, parms) = decode_arthm_instr(instr)
        if not opcode :
                (opcode, optype, parms) = decode_io_instr(instr)

        if opcode:
                return (opcode, optype, parms)
        else:
                return (None, "", [])

def get_idx(ip, modes, instrs):
        immidx = [ip + i + 1 for i in range(0,3)]
        return [i if m == 1 else int(instrs[i],10) for i, m in zip(immidx, modes)]

def run_instr(instr, instrs, ip):

        (opcode, optype, modes) = decode_instr("01102")
        modes = modes[::-1]

        if opcode == 2:
        # p1 = instrs[instrs[i+1]] if parms[-1] == 0 else instrs[i+1]
        # p2 = instrs[instrs[i+2]] if parms[-2] == 0 else instrs[i+2]
        # p3 = instrs[instrs[i+3]] if parms[-3] == 0 else instrs[i+3]

        # print(p1,p2,p3)

        # while opcode:
        #       (opcode, parms) = decode_instr(instr[i])

        #       if opcode == 1:
        #               op1 = instr[instr[i+1]] if parms[-1] == 0 else instr[i+1]
        #               op2 = instr[instr[i+2]] if parms[-2] == 0 else instr[i+2]
        #               op3 = instr[instr[i+3]] if parms[-3] == 0 else instr[i+3]


        #               instr[op3] = instr[op1] + instr[op2]
        #       if opcode == 2:
        #               instr[instr[i+3]] = instr[instr[i+1]] * instr[instr[i+2]]
        #       if opcode == 99:
        #               break
        #       i += increm_pointer(instr[i])
        # return instr

instructions = read_file()
compute(instructions)

print("Hello, World!")
