import sys
import itertools
import numpy as np

def parse_field(field):
    _, nums = field.split(': ')
    a, b = nums.split(' or ')
    c,d = a.split('-')
    e,f = b.split('-')
    return ((int(c),int(d)), (int(e),int(f)))

def is_valid(nums, fields):
    for n in nums:
        valid = False
        for (l, t) in fields:
            if l <= n and n <= t:
                valid = True
                break
        if not valid:
            return False
    return True

def parse_ticket(t):
    return [int(x) for x in t.split(',')]

def check_match(n, field):
    (a,b), (c,d) = field
    return (a <= n and n <= b) or (c <= n and n <= d)

def memoize(f):
    memo = {}
    def helper(x, y):
        if (x,y) not in memo:
            memo[(x,y)] = f(x,y)
        return memo[(x,y)]
    return helper

def get_matches(nums, field):
    if all(check_match(n, field) for n in nums):
        return 1
    else:
        return 0

get_matches = memoize(get_matches)

def assign_fields(tickets, fields):
    if len(tickets) == 0:
        return []
    for i, (field_num, field) in enumerate(fields):
        for j, (ticket_num, ticket)  in enumerate(tickets):
            if get_matches(ticket, field):
                ass = assign_fields(tickets[:j] + tickets[j+1:], fields[:i] + fields[i:1:])
                if ass is not None:
                    return [(field_num, ticket_num)] + ass

def part1(input):
    fields, your, nearby = input.split('\n\n')
    fields = [parse_field(x) for x in fields.split('\n')]
    fields_flat = list(itertools.chain(*fields))
    total = 0
    tickets = [parse_ticket(t) for t in nearby.split('\n')[1:]]
    your = parse_ticket(your.split('\n')[1])
    tickets = [t for t in tickets if is_valid(t, fields_flat)]
    transposed = list(zip(*tickets))
    matrix = [[get_matches(t, field) for t in transposed] for field in fields]
    matrix = np.array(matrix)
    pairs = []
    for _ in range(len(matrix)):
        row = np.where(np.sum(matrix, axis=1) == 1)[0][0]
        col = np.where(matrix[row] == 1)[0][0]
        pairs.append((row, col))
        matrix[row] = 0
        matrix[:, col] = 0
    d = dict(pairs)
    for k, v in d.items():
        print(get_matches(transposed[v], fields[k]))
    print('===')
    prod = 1
    for i in range(6):
        prod *= your[d[i]]

    print('===')
    print(prod)

part1(sys.stdin.read().strip())
