import functools
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

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


solve(open('test.txt').read())
solve(open('real.txt').read())
