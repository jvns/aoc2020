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

def part2(input):
    rules, strings = input.split('\n\n')
    rules = dict(parse(x) for x in rules.split('\n'))
    r42 = regex(42, rules)
    r31 = regex(31, rules)
    # 0: 8 11
    # this is (r42)+
    # 8: 42 | 42 8
    # this is equal numbers of things that match 42 / 31
    # 11: 42 31 | 42 11 31
    total = sum(1 for x in strings.strip().split('\n') if match(x, r42, r31))
    print(total)

def match(x, r42, r31):
    for i in range(1, 30):
        # equal numbers of things that match 42 / 31, so this is a hack to try
        # every possible number. we probably don't need to go as big as 30
        # because the strings aren't that long
        regexp = f"^({r42})+(({r42}){{{i}}}({r31}){{{i}}})$"
        if re.compile(regexp).match(x):
            return True
    return False


def regex(num, rules):
    # wrong guesses: 174, 274
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


part2(sys.stdin.read().strip())
