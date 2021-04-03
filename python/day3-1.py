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

x, y = (0, 0)
x_adv = 3
y_adv = 1
trees = 0

while y < (len(data) - 1):
    x += x_adv
    y += y_adv
    if data[y][x] == '#':
        trees += 1

print(trees)

