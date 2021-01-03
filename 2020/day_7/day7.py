
import re
from collections import defaultdict

def get_input():
    file = open('day7_input', 'r')
    return file.read().splitlines()


def get_bags(line, part):
    bigbag = re.findall("^[a-z]+\s[a-z]+", line)
    ## the number of baggs is not important for part1
    if part == 1:
        smallbags = re.findall("[0-9]+\s([a-z]+\s[a-z]+)", line)
    else:
        smallbags = re.findall("[0-9]+\s[a-z]+\s[a-z]+", line)

    if smallbags:
        return (bigbag, smallbags)
    else:
        return (bigbag, bigbag)

def process_bags_1(lines):
    bags = defaultdict(lambda : set())

    for line in lines:
        ([big], smalls) = get_bags(line, 1)
        #print(big, smalls, big == smalls[0])
        if big != smalls[0]:
            for smallb in smalls:
                bags[smallb].add(big)

    return bags

def process_bags_2(lines):
    bags = defaultdict(lambda : [])

    for line in lines:
        ([big], smalls) = get_bags(line, 2)
        if big == smalls[0]:
            bags[big] = [(1, 'bags')]
        else:
            for sbag in smalls:
                [nr] = re.findall("[0-9]+", sbag)
                [bag] = re.findall("[a-z]+\s[a-z]+", sbag)
                bags[big].append((int(nr), bag))
    return bags


def part1():

    lines = get_input()
    bags = process_bags_1(lines)

    result = set()
    stackb = ['shiny gold']

    while stackb:
        e = stackb.pop()
        result.add(e)
        for sbag in bags[e]:
            stackb.append(sbag) 
        
    print(len(list(result)) - 1)

#part1()

def count_bags(bags, item):

    knownBags = {}
    for k,v in bags.items():
        if v[0][1] == 'bags':
            knownBags[k] = 0
        
    for k in knownBags.keys():
        del bags[k]

    flag = 1
    copyK = None
    
    while flag:
        print(knownBags)
        for k, v in bags.items():
            count = 0
            countKnownBags = 0
            for nr, bag in v:
                if bag in knownBags.keys():
                    count += (nr * knownBags[bag]) + nr
                    countKnownBags += 1
                else:
                    break
            

            if countKnownBags == len(v):
                copyK = k
                copyCount = count
                break
            
        print(copyK)
        if copyK == 'shiny gold':
            flag = 0

        knownBags[copyK] = copyCount
 
        del bags[copyK]

    print(knownBags['shiny gold'])




def part2():
    lines = get_input()
    bags = process_bags_2(lines)
    bcount = defaultdict(lambda : -1)
    for k, v in bags.items():
        print(k, v)
    count_bags(bags, (1, 'shiny gold'))



part2()
