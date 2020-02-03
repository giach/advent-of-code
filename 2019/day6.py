from collections import defaultdict
from collections import Counter
from copy import copy

def read_file():
        lines = []
        with open("day6_small_input") as fp:
                line = fp.readline().rstrip()

                while line:
                        lines += [line.split(")")]
                        line = fp.readline().rstrip()


        return lines

def helper(d, acc, key):
        print(key, d[key])
        if d[key] == []:
                return acc

        for k in d[key]:
                # print("for , ", k)
                return len(d[key]) + helper(d, acc + 1, k)

def part1():
        d = defaultdict(lambda: [])
        dd = defaultdict(lambda: [])
        lines = read_file()

        for t in lines:
                d[t[0]] += [t[1]]


        queue = []
        # key = 'VM4'
        key = 'COM'
        dcopy = copy(d)
        acc = 0;
        print(helper(dcopy, acc, key))
        print(acc)

print("hello mia gia")
print ("tiger ♥")

def rec_fun(n, acc):
        if n == 1:
                return acc

        return rec_fun(n-1, acc*n)


# print(rec_fun(3,1))
part1()
