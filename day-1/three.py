import sys
with open(sys.argv[1]) as f:
    numbers = set(int(x) for x in f.readlines())

def get_add_to(numbers, total):
    inverses = set(total-n for n in numbers)
    return list(inverses.intersection(numbers))

for n in numbers:
    result = get_add_to(numbers, 2020-n)
    if len(result) > 0:
        a,b = result
        print(a * b * n)
        break
