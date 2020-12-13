import sys

file = open(sys.argv[1]).read()


anses = [[set(x for x in line) for line in group.split()] for group in file.split("\n\n")]
yeses = lambda op: sum(len(op(*a)) for a in anses)
part1, part2 = yeses(set.union), yeses(set.intersection)
print(part1, part2)
