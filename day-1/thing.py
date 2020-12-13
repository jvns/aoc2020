import sys
with open(sys.argv[1]) as f:
    numbers = set(int(x) for x in f.readlines())

inverses = set(2020-n for n in numbers)
a, b = list(inverses.intersection(numbers))
print(a * b)



