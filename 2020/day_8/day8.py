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

        # jump by argumen or by one
        if instr == JMP:
            i += arg
        else:
            i += 1
        
        # increment de accumulator
        if instr == ACC:
            acc += arg

        if instr == NOP:
            continue
        


print("The result for Part1 is: ", part1())
