from __future__ import annotations
import math
import sys
from dataclasses import dataclass
import dataclasses
from collections import defaultdict
import numpy as np


def np_rotate(tile):
    rows = np.array([[x for x in line] for line in tile.rows.split('\n')])
    rows = rows[1:-1,1:-1]
    return rot(rows, tile.orientation)

def rot(rows, orientation):
    for _ in range(orientation.rotation):
        rows = np.rot90(rows, axes=(1,0))
    if orientation.flipped:
        rows = np.flip(rows, axis=1)
    return rows

def rotate(edges, n):
    #####
    #   12      87
    #  7  3    5  1
    #  8  4    6  2
    #   56      43
    #
    for _ in range(n):
        t, r, b, l = edges
        edges = (rev(l), t, rev(r), b)
    return edges

def rev(x):
    return ''.join(reversed(x))

def flip(edges):
    t, r, b, l = edges
    return (rev(t), l, rev(b), r)

def flippp(edges):
    return [''.join(reversed(x)) for x in edges]

def orient(edges, orientation):
    edges = rotate(edges, orientation.rotation)
    if orientation.flipped:
        return flip(edges)
    return edges

def all_orientations():
    return [
            Orientation(i, b)
            for i in range(4)
            for b in [True, False]]

@dataclass(frozen=True)
class Orientation:
    rotation: int
    flipped: bool
    def __str__(self):
        if self.flipped:
            return f"{self.rotation}f"
        else:
            return f"{self.rotation}"

@dataclass(frozen=True)
class Tile:
    edges: tuple
    num: int
    rows: str
    orientation: Orientation

    @staticmethod
    def create(num, rows):
        top = rows[0]
        bottom = rows[-1]
        left = ''.join(x[0] for x in rows)
        right = ''.join(x[-1] for x in rows)
        edges = (top, right, bottom, left)
        rows = '\n'.join(rows)
        return Tile(edges, num, rows, Orientation(0, False))

    def possible_edges(self):
        flipped = [''.join(reversed(x)) for x in self.edges]
        return flipped + list(self.edges)

    def oriented_edges(self):
        return orient(self.edges, self.orientation)

    def to_str(self):
        edges = self.oriented_edges()
        s = edges[0]
        middle = len(edges[0]) - 2
        for i in range(1, middle + 1):
            s += '\n' + edges[3][i] + ' ' * middle + edges[1][i]
        s += '\n' + edges[2]
        return s

    def oriented(self, x):
        return dataclasses.replace(self, orientation=x)

    def top_edge(self):
        return self.oriented_edges()[0]

    def right_edge(self):
        return self.oriented_edges()[1]

    def bottom_edge(self):
        return self.oriented_edges()[2]

    def left_edge(self):
        return self.oriented_edges()[3]

    def works(self, left, top):
        # find an orientation that where the left tile is to the left of this tile
        # and the top tile is to the top
        # returns a tile
        le = left.right_edge() if left is not None else None
        te = top.bottom_edge() if top is not None else None
        orientations = all_orientations()
        for orientation in orientations:
            r = orient(self.edges, orientation)
            if (te is None or r[0] == te) and (le is None or r[-1] == le):
                yield self.oriented(orientation)

def parse_tile(tile):
    lines = tile.strip().split('\n')
    num = int(lines[0][5:-1])
    return (num, Tile.create(num, lines[1:]))

def make_edge2tile(all_tiles):
    edge2tile = defaultdict(set)
    for num, tile in all_tiles.items():
        for e in tile.possible_edges():
            edge2tile[e].add(tile)
    return edge2tile

def get_candidates(edge2tile, remaining, top, left):
    if left is not None:
        return remaining.intersection(edge2tile[left.right_edge()])
    if top is not None:
        return remaining.intersection(edge2tile[top.bottom_edge()])
    return remaining.copy()

def print_placed(placed):
    print('___placed___')
    for row in placed:
        print(' '.join([f"{x.num}({x.orientation})" for x in row]))
    print('____________')

def get_top_left(placed, remaining):
    left = None
    top = None
    if len(placed[-1]) > 0:
        left = placed[-1][-1]
    if len(placed) > 1:
        top = placed[-2][len(placed[-1])]
    return (top, left)

def placed_len(placed):
    return sum(len(x) for x in placed)

def insert_tile(placed, remaining, tile, oriented_tile, width):
    placed = [x.copy() for x in placed]
    remaining = remaining.copy()
    placed[-1].append(oriented_tile)
    remaining.remove(tile)
    return placed, remaining


def backtrack(edge2tile, placed_init, remaining_init, width=3):
    if placed_len(placed_init) + len(remaining_init) != width * width:
        print('oh no')
        assert False
    if len(remaining_init) == 0:
        return placed_init
    placed = placed_init.copy()
    remaining = remaining_init.copy()
    if len(placed[-1]) == width:
        placed.append([])
    top, left = get_top_left(placed, remaining)
    for tile in get_candidates(edge2tile, remaining, top, left):
        oriented_tiles = list(tile.works(left, top))
        for oriented_tile in oriented_tiles:
            new_placed, new_remaining = insert_tile(placed, remaining, tile, oriented_tile, width)
            ret = backtrack(edge2tile, new_placed, new_remaining, width=width)
            if ret is not None:
                return ret
    # unnecessary but you know
    #print('backtracking')
    return None

def part1(input):
    all_tiles = dict(parse_tile(t) for t in input.split("\n\n"))
    edge2tile = make_edge2tile(all_tiles)
    width = round(math.sqrt(len(all_tiles)))
    final = backtrack(edge2tile, [[]], set(all_tiles.values()), width=width)
    print_placed(final)
    print(final[0][0].num, final[0][-1].num, final[-1][0].num, final[-1][-1].num)
    print(final[0][0].num* final[0][-1].num* final[-1][0].num* final[-1][-1].num)

def make_array(monster):
    monster = monster.strip()
    return np.array([[x for x in line] for line in monster.split('\n')])


def part2(input):
    all_tiles = dict(parse_tile(t) for t in input.split("\n\n"))
    edge2tile = make_edge2tile(all_tiles)
    width = round(math.sqrt(len(all_tiles)))
    final = backtrack(edge2tile, [[]], set(all_tiles.values()), width=width)
    print_placed(final)
    tile = final[0][0]
    rows = [np.concatenate([np_rotate(tile) for tile in r], axis=1) for r in final]
    rows = np.concatenate(rows)

    monster = make_array("""
^^^^^^^^^^^^^^^^^^#^
#^^^^##^^^^##^^^^###
^#^^#^^#^^#^^#^^#^^^
    """)

    print('----')
    rows = rot(rows, Orientation(3, False))
    for x in rows:
        print(''.join(x))
    print('----')
    print(rows.shape)
    total = 0
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            for o in [Orientation(0, False)]:
            #for o in all_orientations():
                rowsss = rot(rows, o)
                mons = np.full_like(rows, '^')
                try:
                    mons[i:i+monster.shape[0],j:j+monster.shape[1]] = monster
                    count =  np.count_nonzero(mons == rot(rows, o))
                    if count == 15:
                        total += 1
                except:
                    pass
    print(total)
    #print(monster)



part2(sys.stdin.read().strip())
