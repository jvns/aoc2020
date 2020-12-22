import sys
from collections import deque

def score(x):
    print(sum(x*y for x,y in zip(range(1, len(x)+4), reversed(x))))
def play(p1, p2):
    prev_games = set()
    p1 = deque(p1)
    p2 = deque(p2)
    orig_p1 = p1.copy()
    orig_p2 = p2.copy()
    while len(p1) != 0 and len(p2) != 0:
        g = (tuple(p1), tuple(p2))
        if g in prev_games:
            return 1, []
        prev_games.add(g)
        c1, c2 = p1.popleft(), p2.popleft()
        winner = None
        if c1 <= len(p1) and c2 <= len(p2):
            winner, _ = play(list(p1)[:c1], list(p2)[:c2])
        elif c1 > c2:
            winner = 1
        else:
            winner = 2
        if winner == 1:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
        if len(p1) == 0:
            return 2, p2
        elif len(p2) == 0:
            return 1, p1
        #print(p1, p2)

def part1(input):
    p1, p2 = input.split('\n\n')
    p1 = [int(x) for x in p1.strip().split('\n')[1:]]
    p2 = [int(x) for x in p2.strip().split('\n')[1:]]
    winner, l = play(p1, p2)
    print(winner, score(l))
    pass


part1(sys.stdin.read().strip())
