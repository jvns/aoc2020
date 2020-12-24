import sys
from collections import defaultdict
from termcolor import colored

def parse(line):
    def gen(l):
        while len(l) > 0:
            if l[0] in ['e', 'w']:
                yield l[0]
                l = l[1:]
            else:
                yield l[:2]
                l = l[2:]
    return list(gen(line))

def print_tiles(tiles):
    h = '⬢'
    for i in range(-5, 5):
        for j in range(-5, 5):
            p = h
            if tiles[(i,j)] == 1:
                p = colored(h, 'red')
            if i == 0 and j == 0:
                p = colored(h, 'blue')
            if i % 2 == j % 2:
                print(p, end='')
            else:
                print(' ', end='')
        print('')

def adjacent_tile(direction, i, j):
    dirs = {
       'w': (0, -2),
       'e': (0, 2),
       'ne': (-1, 1),
       'nw': (-1, -1),
       'se': (1, 1),
       'sw': (1, -1),
    }
    x, y = dirs[direction]
    return i+x, y+j

def get_candidates(tiles):
    directions = ['w', 'e', 'ne', 'nw', 'se', 'sw']
    def g():
        for i, j in tiles:
            if tiles[(i,j)] != 1:
                continue
            yield (i,j)
            for d in directions:
                yield adjacent_tile(d, i, j)
    return set(g())

def count_black(tiles, i, j):
    total = 0
    directions = ['w', 'e', 'ne', 'nw', 'se', 'sw']
    for d in directions:
        if tiles[adjacent_tile(d, i, j)] == 1:
            total += 1
    return total

def flip(tiles):
    new = defaultdict(int)
    for (i,j) in get_candidates(tiles):
        total = count_black(tiles, i, j)
        if tiles[(i,j)] == 1 and (total == 0 or total > 2):
            new[(i,j)] = 0
        elif tiles[(i,j)] == 0 and total == 2:
            new[(i,j)] = 1
        else:
            new[(i,j)] = tiles[(i,j)]
    return new

def add(tiles, line):
    i, j = 0, 0
    for direction in line:
        i, j = adjacent_tile(direction, i, j)
    tiles[(i,j)] = 1 - tiles[(i,j)]


def part1(input):
    lines = [parse(line) for line in input.split('\n')]
    tiles = defaultdict(int)
    for line in lines:
        add(tiles, line)
    for i in range(100):
        tiles = flip(tiles)
    print(len([x for x in tiles if tiles[x] == 1]))


part1(sys.stdin.read().strip())
