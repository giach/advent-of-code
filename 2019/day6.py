from collections import defaultdict
from collections import Counter
from copy import copy

def read_file():
        lines = []
        with open("day6_input") as fp:
                line = fp.readline().rstrip()

                while line:
                        lines += [line.split(")")]
                        line = fp.readline().rstrip()


        return lines

def helper(d, acc, key):
        #print(key, d[key], acc)
        if d[key] == []:
                return acc

        tmp = acc
        tmp += 1
        for k in d[key]:
                acc += helper(d, tmp, k)
        return acc

def part1():
        d = defaultdict(lambda: [])
        dd = defaultdict(lambda: [])
        lines = read_file()

        keys = set()
        values = set()
        for t in lines:
                keys.add(t[0])
                values.add(t[1])
                d[t[0]] += [t[1]]

        # get the COM
        key = list(keys - values)[0]

        queue = []
        acc = 0;
        s = 0

        s += helper(d, acc, key)

        print(s)

# 301100
part1()
print("hello mia gia")
print ("tiger ♥")
