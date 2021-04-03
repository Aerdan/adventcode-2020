#!/usr/bin/env python3

import sys

data = []

with open('input13.txt') as f:
    for line in f:
        data.append(line.strip())

now = int(data[0])
bus = data[1].split(',')
rts = {int(x): 'D' for x in bus if x != 'x'}

x = sorted(rts.keys())[0]
h, m = 0, x

query = False
while True:
    if x == now:
        query = True
        print(x)
        for route, state in rts.items():
            print(state, route)
    if query:
        print(x, ' '.join(['{}{}'.format(state, route) for route, state in rts.items()]))
    for route in rts.keys():
        if (x % route) == 0:
            rts[route] = 'D'
            if query:
                print(x, route, route * (x - now))
                sys.exit()
        else:
            rts[route] = '.'
    x += 1
