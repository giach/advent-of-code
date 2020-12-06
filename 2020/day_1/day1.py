
from collections import defaultdict

def get_lines():
    file = open('day1_input', 'r')
    lines = file.readlines()
    return lines


def process_input(lines):
    return list(map(lambda x: int(x), lines))


def part1():
    lines = process_input(get_lines())
    nrs = defaultdict(lambda : 0)
    n = len(lines)

    # for i in range(0,n):
    #     if lines[i] > 2020:
    #         continue
    #     for j in range(i+1, n):
    #         if lines[i] + lines[j] == 2020:
    #             return (lines[i], lines[j], lines[i] * lines[j])

    # find in dict the diff between 2020 and currenty number
    # current_nr + (2020 - current_nr) =  2020
    # for k, _ in nrs.items():
    #     if nrs.get(2020 - k, 0) == 1:
    #         return (k, 2020-k, k * (2020-k))

    # Time complexity O(n)
    # Space complexity O(n)
    for e in lines:
        if nrs.get(2020 - e, 0) == 1:
            return (e, 2020 - e, e * (2020 - e))
        else:
            nrs[e] = 1




def part2():
    lines = process_input(get_lines())
    nrs = defaultdict(lambda : 0)
    n = len(lines)

    for e in lines:
        nrs[e] = 1

    for k1, _ in nrs.items():
        for k2, _ in nrs.items():
            if nrs.get(2020 - k1 - k2, 0) == 1:
                return (k1, k2, 2020 - k1 - k2, k1 * k2 * (2020 - k1 - k2))


print(part1())
print(part2())










