#!/usr/bin/env python3

from collections import deque

preamble = 25

q = deque(maxlen=preamble)
x = 0

with open('input9.txt') as f:
    while line := f.readline():
        line = int(line.strip())
        if x < preamble:
            q.append(line)
            x += 1
            continue

        matching = False
        for i in q:
            if (line - i) in q:
                matching = True
                break
        if not matching:
            print(line)
            break

        q.append(line)
