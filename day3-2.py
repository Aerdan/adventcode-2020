#!/usr/bin/env python3

class Ring(list):
    def __getitem__(self, idx):
        while idx >= len(self):
            idx -= len(self)
        ret = super().__getitem__(idx)

        return ret

data = []

with open('input3.txt') as f:
    for line in f.readlines():
        data.append(Ring(line[:-1]))

def checkslope(x_adv, y_adv):
    x, y = (0, 0)
    trees = 0

    while y < (len(data) - 1):
        x += x_adv
        y += y_adv
        if data[y][x] == '#':
            trees += 1

    return trees

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

ret = 1

for slope in slopes:
    r = checkslope(*slope)
    print(r)
    ret *= r

print(ret)

