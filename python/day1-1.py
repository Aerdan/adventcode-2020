#!/usr/bin/env python3

data = None
nums = []

with open('input.txt') as f:
    data = f.readlines()

for line in data:
    num = int(line)
    
    for other in nums:
        if (num + other) == 2020:
            print(num * other)

    nums.append(num)

