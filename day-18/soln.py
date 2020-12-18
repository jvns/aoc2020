import sys
import re

import re

def tokenize(s):
    parts = []
    level =0
    start = 0
    for i, x in enumerate(s):
        if x == '(':
            if level == 0:
                start = i+1
            level += 1
        elif level == 0 and x != ' ':
            if x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                x = int(x)
            parts.append(x)
            start = i+1
        elif x == ')':
            level -= 1
            if level == 0:
                parts.append(tokenize(s[start:i]))
                start = i+1
    return parts


def evaluate(parts):
    if type(parts) is str or type(parts) is int:
        return parts
    if len(parts) == 1:
        return parts[0]
    elif not all(type(x) != list for x in parts):
        return evaluate([evaluate(p) for p in parts])

    for i, x in enumerate(parts):
        if x == '+':
            blah = parts[i-1] + parts[i+1]
            return evaluate(parts[:i-1] + [blah] + parts[i+2:])
    for i, x in enumerate(parts):
        if x == '*':
            return evaluate(parts[:i]) * evaluate(parts[i+1:])



def part2(input):
    total = 0
    for s in input.split('\n'):
        parts = tokenize(s)
        total += evaluate(parts)
    print(total)

part2(sys.stdin.read().strip())
