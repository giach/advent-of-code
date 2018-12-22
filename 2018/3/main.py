import unittest
from array import *

class Rectangle:
    def __init__(self, x, y, lx, ly):
        self.x = x
        self.y = y
        self.lx = lx
        self.ly = ly

r1 = Rectangle(1,3,4,4)
r2 = Rectangle(3,1,4,4)

r3 = Rectangle(5,5,2,2)
r4 = Rectangle(0,0,1,1)

def overlappingRec(r1, r2):
    if r1.x + r1.lx <= r2.x or r2.x + r2.lx <= r1.x:
        return False
    if r1.y + r1.ly <= r2.y or r2.y + r2.ly <= r2.y:
        return False

    if r1.x <= r2.x:
        l = r2.x - r1.x
    else:
        l = r1.x - r2.x

    if r1.y <= r2.y:
        w = r2.y - r1.y
    else:
        w = r1.y - r2.y

    return True

overlappingRec(r1, r2)
overlappingRec(r3,r1)

class BasicTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        r = overlappingRec(r1,r2)
        self.assertTrue(r)

    def test_2(self):
        r = overlappingRec(r3,r1)
        self.assertFalse(r)

    def test(self):
        self.assertFalse(False)


## Day 3 Part 2 ##
lines = [line.rstrip('\n') for line in open('big_input.txt')]
rectangles = [line.split("@")[1] for line in lines]

coordinates = [r.split(":")[0].strip() for r in rectangles]
dimensions =  [r.split(":")[1].strip() for r in rectangles]

pos = []
mySet = set()

fabric = [['0' for i in range(1000)] for j in range(1000)]

elves = [0 for i in range(1401)]
id = 1
for c, d in zip(coordinates, dimensions):
    x = int(c.split(",")[0].strip())
    y = int(c.split(",")[1].strip())

    w = int(d.split("x")[0].strip())
    l = int(d.split("x")[1].strip())

    elves[id] = 1
    for i in range(x, x+w):
        for j in range(y, y+l):
            if fabric[i][j] == '0':
                fabric[i][j] = str(id)
            elif fabric[i][j] == 'x':
                elves[id] = -1
            else:
                elves[id] = -1
                tmp = int(fabric[i][j])
                elves[tmp] = -1
                fabric[i][j] = 'x'
    id += 1

count = 0

for i in range(1401):
        if elves[i] == 1:
            print(elves[i], i)

#if __name__ == '__main__':
#    unittest.main()
