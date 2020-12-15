#!/usr/bin/env python3

insns = []

with open('input14.txt') as f:
    for line in f:
        insns.append(line.strip())

mem = {}

def masker(m, val):
    temp = bin(val)[2:]
    val = list('0' * (36 - len(temp)) + temp)
    for i in range(36):
        if m[i] != 'X':
            val[i] = m[i]
    return int(''.join(val), 2)

mask = None

for line in insns:
    addr, val = line.split(' = ', maxsplit=1)
    if addr == 'mask':
        mask = val
        print('mask set to', mask)
    elif addr.startswith('mem'):
        addr = int(addr[4:-1])
        mem[addr] = masker(mask, int(val))
        print('mem[{}] set to'.format(addr), mem[addr])

print(sum(mem.values()))
