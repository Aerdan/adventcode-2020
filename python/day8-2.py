#!/usr/bin/env python3

class Buffer(list):
    def __init__(self, iterable):
        self._code = {i: 0 for i in range(len(iterable))}
        super().__init__(iterable)

    def __getitem__(self, key):
        while key >= len(self):
            key -= len(self)
        while key < 0:
            key += len(self)
        val = super().__getitem__(key)
        self._code[key] += 1
        return val

    def __setitem__(self, key, val):
        while key >= len(self):
            key -= len(self)
        while key < 0:
            key += len(self)
        self._code[key] = 0
        super().__setitem__(key, val)

    def used(self, key):
        while key > len(self):
            key -= len(self)
        while key < 0:
            key += len(self)
        return self._code[key]

code = None

with open('input8.txt') as f:
    code = [line[:-1] for line in f.readlines()]

def hotpatch(line):
    global code
    op = code[line]
    if op.startswith('nop'):
        code[line] = op.replace('nop', 'jmp')
    elif op.startswith('jmp'):
        code[line] = op.replace('jmp', 'nop')

# this was bruteforced by manually going through the unmodified program and 
# rerunning this script.
hotpatch(441)
l = len(code)
code = Buffer(code)
x = 0
a = 0
try:
    while line := code[x]:
        if code.used(x) > 1:
            print('-> ', line, '<-', x)
            break
        print(x, line)
        insn, arg = line.split(' ', maxsplit=1)
        arg = int(arg)
        if insn == 'jmp':
            x += arg
        elif insn == 'acc':
            a += arg

        if insn != 'jmp':
            x += 1
except IndexError:
    print(a)

print(l)
print(a)
