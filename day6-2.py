#!/usr/bin/env python3

from collections import Counter

q = {}

with open('input6.txt') as f:
    g = Counter()
    gn = 1
    n = 0

    while line := f.readline():
        line = line[:-1]
        if not len(line):
            q[gn] = sum(1 for i in g.keys() if g[i] == n)
            g = Counter()
            gn += 1
            n = 0
            continue

        g.update(line)
        n += 1
    q[gn] = sum(1 for i in g.keys() if g[i] == n)

print(sum(q.values()))

