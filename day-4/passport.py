import sys
import re

with open(sys.argv[1]) as f:
    passports = f.read().split('\n\n')

required = set([
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    #'cid',
])


def check_year(field, min, max):
    return re.match('^\d\d\d\d$', field) and int(field) >= min and int(field) <= max

def check_height(height):
    if not re.match('\d+(cm|in)', height):
        return False
    h = int(height[:-2])
    if height.endswith('cm'):
        return h >= 150 and h <= 193
    else:
        return h >= 59 and h <= 76


def valid(p):
    p = dict(x.split(':') for x in p.split())
    if set(p.keys()).intersection(required) != required:
        return False
    return all([
        p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        check_year(p['byr'], 1920, 2002),
        check_year(p['iyr'], 2010, 2020),
        check_year(p['eyr'], 2020, 2030),
        check_height(p['hgt']),
        re.match('^#[0-9a-f]{6}$', p['hcl']),
        re.match('^[0-9]{9}$', p['pid']),
    ])


print(sum(1 for p in passports if valid(p)))
