#!/usr/bin/env python3

import sys

class Board:
    def __init__(self, data):
        self._data = tuple([tuple(x) for x in data])
        # assume width of first row is width of all rows
        self._width = len(data[0])
        self._height = len(data)

    def iterate(self):
        new = [list(x) for x in self._data]

        for y in range(self._height):
            for x in range(self._width):
                cell = new[y][x]
                if cell == '.':
                    continue

                occupied = 0

                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        if not (0 <= (y + i) < self._height and
                                0 <= (x + j) < self._width):
                            continue
                        if i == j == 0:
                            continue
                        t = None
                        try:
                            t = self._data[y + i][x + j]
                        except IndexError:
                            continue

                        if t == '#':
                            occupied += 1
                if cell == '#' and occupied >= 4:
                    new[y][x] = 'L'
                elif cell == 'L' and occupied == 0:
                    new[y][x] = '#'

        final = tuple([tuple(x) for x in new])

        if hash(final) == hash(self._data):
            self._data = final
            return False
        else:
            self._data = final
            return True

    def find_occupied(self):
        i = 0
        for y in range(self._height):
            for x in range(self._width):
                if self._data[y][x] == '#':
                    i += 1
        return i

    def print_board(self):
        for line in self._data:
            print(''.join(line))

data = []

with open('input11.txt') as f:
    for line in f:
        data.append(list(line.strip()))

b = Board(data)
x = 0
while b.iterate():
    x += 1
occupied = b.find_occupied()
print('{} empty seats after {} iterations'.format(occupied, x))
