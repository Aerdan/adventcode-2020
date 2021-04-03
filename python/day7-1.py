#!/usr/bin/env python3

bags = {}

with open('input7.txt') as f:
    while line := f.readline():
        line = line[:-1]
        left, right = line.split(' contain ', maxsplit=1)
        left = ' '.join(left.split(' ')[:2])
        right = right.split(', ')
        if right[0].startswith('no'):
            right = ['no']
        else:
            right = [' '.join(item.split(' ')[1:3]) for item in right]

        for bag in right:
            if bag in bags:
                bags[bag].append(left)
            else:
                bags[bag] = [left]

paths = [('shiny gold',)]
desired = 'shiny gold'
finals = []

while len(paths) > 0 and (path := paths.pop(0)):
    color = path[-1]
    if color in bags.keys():
        for n in bags[color]:
            paths.append(path + (n,))
    else:
        finals.append(path)

intermediates = set()
[intermediates.update(path[1:]) for path in finals]

[print(path) for path in finals]
print(len(intermediates))
