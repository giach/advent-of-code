

def get_lines():
    file = open('day3_input', 'r')
    lines = file.readlines()
    n = len(lines)

    for i in range(n):
        lines[i] = list(lines[i].rstrip("\n"))

    return lines



def part2():

    lines = get_lines()
    n = len(lines)
    m = len(lines[0])

    
    result = 1
    ix = [1, 1, 1, 1, 2]
    steps = [1, 3, 5, 7, 1]
    nsteps = len(steps)

    for k in range(0, nsteps):
        i = ix[k]
        step = steps[k]
        count = 0

        while i < n:
            line = lines[i]
            if line[step] == '#':
                count += 1
            step = (step + steps[k]) % m
        
            i = i + ix[k]
        
        result *= count

    print (result)



part2()