import sys

def part1(input):
    num1, num2 = [int(x) for x in input.split()]
    x = 1
    p = 20201227
    for i in range(1, 10000000):
        x = x * 7
        x = x % p
        if x == num1:
            print((num2 ** i) % p)
            break
        elif x == num2:
            print((num1 ** i) % p)
            break


part1(sys.stdin.read().strip())
