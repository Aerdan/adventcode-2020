#!/usr/bin/env python3

data = None
nums = []

with open('input.txt') as f:
    data = f.readlines()

for line in data:
    num = int(line)
    
    for other in nums:
        for third in nums:
            if other == third:
                continue
            if (num + other + third) == 2020:
                print(num * other * third)

    nums.append(num)

