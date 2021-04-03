#!/usr/bin/env python3

def binary(code, max, bits):
    ret = []

    for i in range(max):
        ret.append(bits[code[i]])

    return int(''.join(ret), base=2)

mid = 0

with open('input5.txt') as f:
    for line in f.readlines():
        line = line[:-1]
        row = binary(line[:7], 7, {'F': '0', 'B': '1'})
        col = binary(line[7:], 3, {'R': '1', 'L': '0'})
        sid = row * 8 + col
        mid = sid if sid > mid else mid

print(mid)

