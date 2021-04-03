#!/usr/bin/env python3

def getid():
    global data

    fields = {}

    if not len(data):
        return None

    while len(data) > 0:
        line = data.pop(0)
        if not (len(line) > 1):
            break
        line = line[:-1].split(' ')
        for field in line:
            label, entry = field.split(':', maxsplit=1)
            fields[label] = entry

    return fields

def validate(passport):
    needed = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    for i in needed:
        if i not in passport:
            return False
    return True

data = None

with open('input4.txt') as f:
    data = f.readlines()

validity = 0

while (passport := getid()) and passport is not None:
    if validate(passport):
        validity += 1
    else:
        print('present keys: {}'.format(' '.join(sorted(passport.keys()))))

print(validity)

