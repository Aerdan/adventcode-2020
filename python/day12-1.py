#!/usr/bin/env python3

data = []

with open('input12.txt') as f:
    for line in f:
        data.append(line.strip())

x, y = 0, 0
d = 'E'

c = 'NESW'

for line in data:
    insn = line[0]
    dist = int(line[1:])

    if insn == 'F':
        insn = d
    if insn == 'N':
        y += dist
    elif insn == 'E':
        x += dist
    elif insn == 'S':
        y -= dist
    elif insn == 'W':
        x -= dist
    elif insn == 'L':
        r = c.index(d) - int(dist / 90)
        if r > 3:
            r -= 4
        if r < 0:
            r += 4
        d = c[r]
    elif insn == 'R':
        r = c.index(d) + int(dist / 90)
        if r > 3:
            r -= 4
        if r < 0:
            r += 4
        d = c[r]

md = abs(x) + abs(y)
print(x, y, md)
