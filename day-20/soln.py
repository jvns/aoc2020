from __future__ import annotations
import sys
from dataclasses import dataclass
import dataclasses
from collections import defaultdict

def rotate(tpl, n):
    return tpl[n:] + tpl[:n]

def flip(edges):
    t, r, b, l = edges
    return (t, str(reversed(r)), b, str(reversed(l)))

@dataclass(frozen=True)
class Orientation:
    rotation: int
    flipped: bool

@dataclass(frozen=True)
class Tile:
    edges: tuple
    num: int
    orientation: Orientation

    @staticmethod
    def create(num, rows):
        top = rows[0]
        bottom = rows[-1]
        left = ''.join(x[0] for x in rows)
        right = ''.join(x[1] for x in rows)
        edges = (top, right, bottom, left)
        return Tile(edges, num, Orientation(0, False))

    def possible_edges(self):
        flipped = [str(reversed(x)) for x in self.edges]
        return flipped + list(self.edges)

    def oriented_edges(self):
        edges = rotate(self.edges, self.orientation.rotation)
        if self.orientation.flipped:
            edges = flip(edges)
        return edges

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
        for i in range(4):
            # don't need oriented edges here bc by definition it hasn't been
            # oriented if not placed
            r = rotate(self.edges, i)
            if (te is None or r[0] == te) and (le is None or r[3] == le):
                orientation = Orientation(i, False)
                return self.oriented(orientation)
        for i in range(4):
            r = rotate(self.edges, i)
            r = flip(r)
            if (te is None or r[0] == te) and (le is None or r[3] == le):
                orientation = Orientation(i, True)
                return self.oriented(orientation)

def parse_tile(tile):
    lines = tile.strip().split('\n')
    num = int(lines[0][5:-1])
    return (num, Tile.create(num, lines[1:]))

def make_edge2tile(all_tiles):
    edge2tile = defaultdict(set)
    for num, tile in all_tiles.items():
        for e in tile.possible_edges():
            edge2tile[e].add(num)
    return edge2tile

def get_candidates(edge2tile, remaining, top, left):
    return remaining.copy()

def print_placed(placed):
    print('___')
    for row in placed:
        print(' '.join([str(x.num) for x in row]))

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

def try_tile(placed, remaining, top, left, tile, width):
    if placed_len(placed) + len(remaining) != width * width:
        print('########## MISMATCH ######################')
        print_placed(placed)
        print('remainings', list(sorted([r.num for r in remaining])))
        print(len(remaining))
        print('##########################################')
        assert False
    placed = [x.copy() for x in placed]
    remaining = remaining.copy()
    # TODO: what if there's more than one way a tile could work?
    oriented_tiles = tile.works(left, top)
    if oriented_tile:
        placed[-1].append(oriented_tile)
        remaining.remove(tile)
        return placed, remaining


def backtrack(edge2tile, placed_init, remaining_init, width=3):
    if placed_len(placed_init) + len(remaining_init) != width * width:
        print('oh no')
        assert False
    if len(remaining_init) == 0:
        return placed_init
    print_placed(placed_init)
    placed = placed_init.copy()
    remaining = remaining_init.copy()
    if len(placed[-1]) == width:
        print('adding new row')
        placed.append([])
    top, left = get_top_left(placed, remaining)
    for tile in get_candidates(edge2tile, remaining, top, left):
        result = try_tile(placed, remaining, top, left, tile, width)
        if result:
            new_placed, new_remaining = result
            ret = backtrack(edge2tile, new_placed, new_remaining, width=width)
            if ret is not None:
                return ret
    # unnecessary but you know
    print('backtracking')
    return None

def part1(input):
    all_tiles = dict(parse_tile(t) for t in input.split("\n\n"))
    edge2tile = make_edge2tile(all_tiles)
    for num in all_tiles.keys():
        pass
    final = backtrack(edge2tile, [[]], set(all_tiles.values()), width=3)
    print(len(final))
    for x in final:
        print (list(y.num for y in x))
    print(final[0][0].num, final[0][-1].num, final[-1][0].num, final[-1][-1].num)

    #tile2tile = defaultdict(set)
    #for edge, tiles in edge2tile.items():
    #    for t in tiles:
    #        tile2tile[t] |= tiles
    #        tile2tile[t].remove(t)
    #print(len(edge2tile))
    #for t, adjacent in tile2tile.items():
    #    print(t, adjacent)



part1(sys.stdin.read().strip())
