#!/usr/bin/env python3

q = {}

with open('input6.txt') as f:
    g = {}
    gn = 1

    for line in f.readlines():
        line = line[:-1]
        if not len(line):
            q[gn] = g.keys()
            g = {}
            gn += 1

        for i in line:
            if i not in g:
                g[i] = 1
            else:
                g[i] += 1
    q[gn] = g.keys()

print(sum(len(q[n]) for n in q.keys()))

