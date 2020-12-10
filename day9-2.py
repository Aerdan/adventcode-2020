#!/usr/bin/env python3

from collections import deque

preamble = 25

q = deque(maxlen=preamble)
x = 0
invalid = 0
data = None

with open('input9.txt') as f:
    data = f.readlines()

for line in data:
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
        invalid = line
        break

    q.append(line)

length = len(data)
for i in range(length):
    data[i] = int(data[i])
for i in range(length):
    for j in range(length-i):
        if sum(data[i:j]) == invalid:
            print(min(data[i:j]) + max(data[i:j]))
            break

