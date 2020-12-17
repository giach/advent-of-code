

import re

def get_passports():
    file = open('day4_input', 'r')
    content = file.read().split("\n\n")

    return content


def valid_year(x, y1, y2):
    try:
        return int(x) >= y1 and int(x) <= y2
    except ValueError:
        return False

def valid_pid(x):
    if len(re.findall("[0-9]{9}", x)) == 0:
        return False
    return len(re.findall("[0-9]{9}", x)[0]) == len(x)

def valid_hair_color(x):
    if len(re.findall("^#[0-9a-z]+", x)) == 0:
        return False
    return len(re.findall("^#[0-9a-z]+", x)[0]) == len(x)

def valid_eye_color(x):
    return x in ["amb","blu","brn","gry","grn","hzl","oth"]

def valid_height(x):
    if len(re.findall("^[0-9]{3}cm$", x)) == 1:
        return int(x[:3]) >= 150 and int(x[:3]) <= 193

    if len(re.findall("^[0-9]{2}in$", x)) == 1:
        return int(x[:2]) >= 59 and int(x[:2]) <= 76


def get_pass_fields():
    return ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

def get_fields_and_rule():
    return {"byr": lambda x: valid_year(x, 1920, 2002),
            "iyr": lambda x: valid_year(x, 2010, 2020),
            "eyr": lambda x: valid_year(x, 2020, 2030), 
            "hgt": lambda x: valid_height(x),
            "hcl": lambda x: valid_hair_color(x),
            "ecl": lambda x: valid_eye_color(x),
            "pid": lambda x: valid_pid(x)}


def part1():

    passports = get_passports()
    fields = get_pass_fields()
    n = len(passports)

    for p in passports:
        for f in fields:
            r = re.findall(f, p)
            if r == []:
                n = n - 1
                break

    print(n)
        

def part2():
    passports = get_passports()
    fields = get_pass_fields()
    n = len(passports)
    field_no = 0
    wrong_pass = 0

    rules = get_fields_and_rule()

    for p in passports:
        line = p.split("\n")
        for l in line:
            fields = l.split(" ")
            for f in fields:
                [name, value] = f.split(":")
                if name == "cid":
                    continue
                if rules[name](value) == True:
                    field_no += 1 
        if field_no < 7:
            wrong_pass += 1
        field_no = 0

    print(n - wrong_pass)




part2()
