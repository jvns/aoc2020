import sys
from collections import deque

def score(x):
    print(sum(x*y for x,y in zip(range(1, len(x)+4), reversed(x))))
def play(p1, p2):
    p1 = deque(p1)
    p2 = deque(p2)
    while len(p1) != 0 and len(p2) != 0:
        c1, c2 = p1.popleft(), p2.popleft()
        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
        print(p1, p2)
    print(score(p1))
    print(score(p2))

def part1(input):
    p1, p2 = input.split('\n\n')
    p1 = [int(x) for x in p1.strip().split('\n')[1:]]
    p2 = [int(x) for x in p2.strip().split('\n')[1:]]
    play(p1, p2)
    pass


part1(sys.stdin.read().strip())
