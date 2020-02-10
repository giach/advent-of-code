from collections import defaultdict
from collections import Counter
from copy import copy

def read_file(file_name):
        lines = []
        with open(file_name) as fp:
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
        lines = read_file("day6_input")

        keys = set()
        values = set()
        for t in lines:
                keys.add(t[0])
                values.add(t[1])
                d[t[0]] += [t[1]]

        # get the COM
        key = list(keys - values)[0]

        s = 0
        s += helper(d, 0, key)

        print("Result", s)


def part2():
        ing = defaultdict(lambda: [])
        outg = defaultdict(lambda: [])
        lines = read_file("day6_input_2")

        for t in lines:
                ing[t[0]] += [t[1]]
                outg[t[1]] += [t[0]]

        inyou = outg['YOU'][0]
        print(inyou, ing[inyou][0])

# 301100
part1()

part2()
print ("tiger ♥")
