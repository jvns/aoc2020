from __future__ import annotations
import sys
from dataclasses import dataclass
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

@dataclass
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

    def edges(self):
        normal = self.edges
        flipped = [str(reversed(x)) for x in normal]
        return flipped + normal

    def oriented_edges(self):
        edges = rotate(self.edges, self.orientation.rotation)
        if self.orientation.flipped:
            edges = flip(edges)
        return edges

    def oriented(self, x):
        return dataclasses.replace(self, orientation=x)

    def oriented_edges(self):
        return oriented_edges(self.edges, self.orientation)


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
    return (num, Tile(num, lines[1:]))

def make_edge2tile(all_tiles):
    edge2tile = defaultdict(set)
    for num, tile in all_tiles.items():
        for e in tile.edges():
            edge2tile[e].add(num)
    return edge2tile

def get_candidates(edge2tile, remaining, top, left):
    return remaining

def backtrack(edge2tile, placed, remaining, width=3):
    if len(remaining) == 0:
        return placed
    placed = placed.copy()
    remaining = remaining.copy()
    if len(placed[-1]) == width:
        left = None
        placed.append([])
    else:
        left = placed[-1][-1]
    #####
    #
    if len(placed) > 1:
        top = placed[-2][len(placed[-1])]
    for tile in get_candidates(edge2tile, remaining, top, left):
        # TODO: what if there's more than one way a tile could work?
        oriented_tile = tile.works(left, top)
        if oriented_tile:
            placed[-1].add(oriented_tile)
            remaining.remove(tile)
            ret =  backtrack(edge2tile, placed, remaining, width=3)
            if ret is not None:
                return ret

def part1(input):
    all_tiles = dict(parse_tile(t) for t in input.split("\n\n"))
    edge2tile = make_edge2tile(all_tiles)
    for num in all_tiles.keys():
        pass

    #tile2tile = defaultdict(set)
    #for edge, tiles in edge2tile.items():
    #    for t in tiles:
    #        tile2tile[t] |= tiles
    #        tile2tile[t].remove(t)
    #print(len(edge2tile))
    #for t, adjacent in tile2tile.items():
    #    print(t, adjacent)



part1(sys.stdin.read().strip())
