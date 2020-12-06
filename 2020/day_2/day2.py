
import re

def get_lines():
    file = open('day2_input', 'r')
    lines = file.readlines()

    return lines

def process_line(line):
    [minval, maxval] = re.findall("\d{1,2}", line)
    [char] = re.findall("\s([a-z]):", line)
    [password] = re.findall(":\s(.*)", line)

    return (int(minval), int(maxval), char, password)

    
def part1():
    lines = get_lines()

    validPasswords = 0
    for line in lines:
        (minval, maxval, char, password) = process_line(line)
        occ = re.findall(char, password)
        if len(occ) <= maxval and len(occ) >= minval:
            validPasswords += 1

    # The number of valid passwords
    print(validPasswords)



def part2():
    lines = get_lines()

    validPasswords = 0

    for line in lines:
        (minval, maxval, char, password) = process_line(line)
        if password[minval - 1] == char and password[maxval - 1] != char:
            validPasswords += 1
        if password[minval - 1] != char and password[maxval - 1] == char:
            validPasswords += 1

    print(validPasswords)


part1()

part2()