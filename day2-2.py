#!/usr/bin/env python3

from collections import Counter

data = None

def checkpw(policy, pw):
    limit, req = policy.split(' ', maxsplit=1)
    mini, maxi = limit.split('-', maxsplit=1)
    pos1 = int(mini)
    pos2 = int(maxi)

    if req not in pw:
        return False

    if pw[pos1 - 1] == pw[pos2 - 1] == req:
        return False
    elif pw[pos1 - 1] == req or pw[pos2 - 1] == req:
        return True

    return False

with open('input2.txt') as f:
    data = f.readlines()

valid = 0
for line in data:
    policy, pw = line.split(': ', maxsplit=1)
    if checkpw(policy, pw):
        valid += 1

print(valid)
    
