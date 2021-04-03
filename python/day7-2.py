#!/usr/bin/env python3

bags = {}

with open('input7.txt') as f:
    while line := f.readline():
        line = line[:-1]
        left, right = line.split(' contain ', maxsplit=1)
        left = ' '.join(left.split(' ')[:2])
        right = right.split(', ')
        if right[0].startswith('no'):
            right = (0,)
            bags[left] = [right]
        else:
            bags[left] = []
            for item in right:
                count, item = item.split(' ', maxsplit=1)
                item = item.replace(' bags', '').replace(' bag', '').replace('.', '')
                bags[left].append((int(count), item))

count = 0
paths = [('shiny gold',)]

while len(paths) > 0 and (path := paths.pop(0)):
    color = path[-1]
    for bag in bags[color]:
        count += bag[0]
        if bag[0] == 0:
            continue
        [paths.append(path + (bag[1],)) for i in range(bag[0])]

print(count)
