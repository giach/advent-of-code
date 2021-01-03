import re

NOP = "nop"
ACC = "acc"
JMP = "jmp"

def get_input():

    file = open('day8_input', 'r')
    lines = file.read().splitlines()
    return lines


def process_line(line):
    [instr] = re.findall("^[a-z]+", line)
    [arg] = re.findall("[+|-][0-9]+", line)

    return (instr, int(arg), False)

def process_input(lines):
    instrs = {}
    i = 0

    for line in lines:
        instrs[i] = process_line(line) 
        i += 1

    return instrs

def part1():
    lines = get_input()
    instructions = process_input(lines)
    acc = 0
    i = 0

    while True:
        instr, arg, visited = instructions[i]
        
        # instruction was already executed
        if visited == True:
            return acc

        # mark the instruction as executed
        instructions[i] = (instr, arg, True)

        if instr == JMP:
            i += arg
        elif instr == ACC:
            acc += arg
            i += 1
        elif instr == NOP:
            i += 1
        

def part2():
    lines = get_input()
    instructions = process_input(lines)

    n = len(instructions)

    for idx in range(n):
        instructions = process_input(lines)
        acc = 0
        i = 0
        c_instr, c_arg, c_v = instructions[idx]

        if c_instr == JMP:
            c_instr = NOP
        elif c_instr == NOP:
            c_instr = JMP

        instructions[idx] = c_instr, c_arg, c_v

        while True:
            instr, arg, visited = instructions[i]

            # instruction was already executed
            if visited == True:
                break

            # mark the instruction as executed
            instructions[i] = (instr, arg, True)

            if instr == JMP:
                i += arg
            elif instr == ACC:
                acc += arg
                i += 1
            elif instr == NOP:
                i += 1

            if i >= n:
                return acc

        if c_instr == JMP:
            c_instr = NOP
        elif c_instr == NOP:
            c_instr = JMP

        instructions[idx] = c_instr, c_arg, c_v


print("The result for Part 1 is: ", part1())
print("The result for Part 2 is: ", part2())
