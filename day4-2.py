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


def rangevalidator(min, max):
    def validator(field):
        try:
            field = int(field)
        except ValueError:
            return False

        return min <= field <= max

    return validator

def hgt(field):
    hgtin = rangevalidator(59, 76)
    hgtcm = rangevalidator(150, 193)
    if field[-2:] == 'cm':
        return hgtcm(field[:-2])
    elif field[-2:] == 'in':
        return hgtin(field[:-2])
    else:
        return False

def hcl(field):
    if not field.startswith('#'):
        return False

    x = 0
    for i in field[1:]:
        x += 1
        if i not in '0123456789abcdefABCDEF':
            return False

    if x != 6:
        return False
    return True

def ecl(field):
    return field in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def pid(field):
    return len(field) == 9

validators = {
    'byr': rangevalidator(1920, 2002),
    'iyr': rangevalidator(2010, 2020),
    'eyr': rangevalidator(2020, 2030),
    'hgt': hgt,
    'hcl': hcl,
    'ecl': ecl,
    'pid': pid
}

def validate(passport):
    for field in validators.keys():
        if field not in passport.keys():
            return False
        if not validators[field](passport[field]):
            return False
    return True

data = None

with open('input4.txt') as f:
    data = f.readlines()

validity = 0

while (passport := getid()) and passport is not None:
    if validate(passport):
        validity += 1

print(validity)

