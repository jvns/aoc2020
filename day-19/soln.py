import sys

def parse_rule(rule):
    if rule.startswith('"'):
        return rule[1:-1]
    if '|' in rule:
        print(rule)
        a,b  = rule.split(' | ')
        c,d = a.split()
        e,f = b.split()
        return ((int(c), int(d)), (int(e), int(f)))
    return [int(x) for x in rule.split()]


def parse(line):
    idx, rule = line.split(':')
    return int(idx), parse_rule(rule.strip())

import re

def part1(input):
    rules, strings = input.split('\n\n')
    rules = dict(parse(x) for x in rules.split('\n'))
    #print(rules)
    reg = '^' + regex(0, rules) + '$'
    print(reg)
    reg = re.compile(reg)
    total = sum(1 for x in strings.strip().split('\n') if reg.match(x))
    print(total)

def regex(num, rules):
    rule = rules[num]
    if type(rule) is str:
        return rule
    if type(rule) is list:
        return ''.join(regex(x, rules) for x in rule)
    if type(rule) is tuple:
        (a,b), (c,d) = rule
        a_rex = regex(a, rules)
        b_rex = regex(b, rules)
        c_rex = regex(c, rules)
        d_rex = regex(d, rules)
        return f"(({a_rex}{b_rex})|({c_rex}{d_rex}))"


part1(sys.stdin.read().strip())
