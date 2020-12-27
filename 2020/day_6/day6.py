def get_groups():
    file = open('day6_input', 'r')

    groups = file.read().split("\n\n")

    return groups




def part1():

    groups = get_groups()
    answers = 0

    for g in groups:
        ans = set()
        people = g.split("\n")
        for p in people:
            for a in list(p):
                ans.add(a)

        answers += len(list(ans))

    print(answers)


def part2():

    groups = get_groups()
    answers = 0

    for g in groups:
        common = set()
        people = g.split("\n")
        for a in list(people)[0]:
            common.add(a)
        for i in range(1, len(people)):
            ans = set()
            for a in list(list(people)[i]):
                ans.add(a)
            common = common.intersection(ans)
        
        print(len(common), common)
        answers += len(list(common))

    print(answers)

part2()