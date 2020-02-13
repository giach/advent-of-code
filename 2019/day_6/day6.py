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

        print("Part 1 result", s)



def min_transfers(d, start, dest):

        # direct nodes are on level 0
        q = [(n, 0) for n in d[start]]
        visited = [start]
        while q:
                elem, level = q.pop(0)
                if not elem in visited:
                        if elem == dest:
                                return level - 1
                        else:
                                q += [(n, level + 1) for n in d[elem]]
                                visited += [elem]

        return None

def part2():
        orbits = defaultdict(lambda: [])
        lines = read_file("day6_input_2")

        for t in lines:
                orbits[t[0]] += [t[1]]
                orbits[t[1]] += [t[0]]

        level = min_transfers(orbits, 'YOU', 'SAN')
        print("Part 2 result", level)




# 301100
part1()

# 547
part2()
print ("tiger ♥")
