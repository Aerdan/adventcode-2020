#!/usr/bin/env python3

data = [0]

with open('input10.txt') as f:
    for line in f:
        data.append(int(line.strip()))

data.sort()

jolt1 = 0
jolt3 = 0

for i in range(len(data)):
    try:
        data[i + 1]
    except IndexError:
        jolt3 += 1
        break
    if data[i + 1] - data[i] == 1:
        jolt1 += 1
    if data[i + 1] - data[i] == 3:
        jolt3 += 1

print(jolt1, jolt3, jolt1 * jolt3)
