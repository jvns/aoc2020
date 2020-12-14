import sys
import functools

def modinv(a, m):
    for i in range(0, m):
        if a * i % m == 1:
            return i

def mod_a_b(x, y):
    moda, a = x
    modb, b = y
    inv = modinv(a, b)
    return (moda + inv*a*(modb - moda), a * b)

def solve(input):
    line1, line2 = input.strip().split()
    buses = [(-i, int(bus_id)) for i,bus_id in enumerate(line2.split(',')) if bus_id != 'x']
    mod, x = functools.reduce(mod_a_b, buses)
    print(mod % x)


solve(sys.stdin.read().strip())
