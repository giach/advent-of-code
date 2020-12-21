



def get_steps():
    file = open("day5_input", "r")

    lines = file.read().splitlines()

    return lines


def part1():
    lines = get_steps()
    seats =  []

    maxid = -999999
    rowsum = 0
    seats = []
    exitingseats = 0

    for line in lines:
        row = 0
        column = 0
        pline = list(line)
        for i in pline:
            if i == 'F':
                row = row << 1
            if i == 'B':
                row = (row << 1) + 1
            if i == 'L':
                column = column << 1
            if i == 'R':
                column = (column << 1) + 1

        seat = row * 8 + column
        exitingseats += seat
        if (seat) > maxid:
            maxid = seat
        seats.append(seat)

    sorted_seats = sorted(seats)

    # these are the seats which do not exist from the
    # very front and back of the plane
    lowseats = sum(list(range(sorted_seats[0])))
    highseats = sum(list(range(sorted_seats[-1] + 1, 1024)))

    # all possible exiting seats
    allseats = sum(list(range(1024)))

    # remove the non existing seats and the seats from
    # my list to find out what is my place
    # Part2 - my seat ID
    print("Part2 - my seat ID: ", allseats - lowseats - highseats - exitingseats)

    # Part1 - max seat ID
    print("Part1 - max seat ID: ", maxid)


# this has also part2
part1()
