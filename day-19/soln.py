import sys

def parse_rule(rule):
    if rule.startswith('"'):
        return rule[1:-1]
    elif '|' in rule:
        a,b  = rule.split(' | ')
        return ([int(x) for x in a.split()], [int(x) for x in b.split()])
    else:
        return [int(x) for x in rule.split()]


def parse(line):
    idx, rule = line.split(':')
    return int(idx), parse_rule(rule.strip())

import re

def part1(input):
    rules, strings = input.split('\n\n')
    rules = dict(parse(x) for x in rules.split('\n'))
    reg = '^' + regex(0, rules) + '$'
    print(reg)
    # 0: 8 11
    # 8: 42 | 42 8
    # 11: 42 31 | 42 11 31
    reg = re.compile(reg)
    total = sum(1 for x in strings.strip().split('\n') if reg.match(x))
    print(total)

def regex(num, rules):
    rule = rules[num]
    if type(rule) is str:
        return rule
    elif type(rule) is list:
        return ''.join(regex(x, rules) for x in rule)
    elif type(rule) is tuple:
        left, right = rule
        left = ''.join(regex(x, rules) for x in left)
        right = ''.join(regex(x, rules) for x in right)
        return f"({left}|{right})"


part1(sys.stdin.read().strip())
