#!/usr/bin/env python3

from math import sin, cos, radians

data = []

with open('input12.txt') as f:
    for line in f:
        data.append(line.strip())

x, y = 10, 1
sx, sy = 0, 0
d = 'E'

c = 'NESW'

for line in data:
    insn = line[0]
    dist = int(line[1:])

    if insn == 'F':
        # move to waypoint dist times
        for i in range(dist):
            sx += x
            sy += y
    elif insn == 'N':
        y += dist
    elif insn == 'E':
        x += dist
    elif insn == 'S':
        y -= dist
    elif insn == 'W':
        x -= dist
    elif insn == 'L':
        dist = radians(dist)
        nx = x * cos(dist) - y * sin(dist)
        ny = y * cos(dist) + x * sin(dist)
        x = round(nx)
        y = round(ny)
    elif insn == 'R':
        dist = radians(360 - dist)
        nx = x * cos(dist) - y * sin(dist)
        ny = y * cos(dist) + x * sin(dist)
        x = round(nx)
        y = round(ny)

md = abs(sx) + abs(sy)
print(sx, sy, md)
