import re

def parse(line):
    instr,  n = re.match('^(...) (.\d+)$', line).groups()
    return (instr, int(n))

def solve(input):
    lines = [parse(line) for line in input.strip().split('\n')]
    for i in range(len(lines)):
        instr, n = lines[i]
        if instr == 'jmp':
            x = lines.copy()
            x[i] = ('nop', n)
            term, acc = terminates(x)
            if term:
                print(acc)
                return
        if instr == 'nop':
            x = lines.copy()
            x[i] = ('jmp', n)
            term, acc = terminates(x)
            if term:
                print(acc)
                return




    print(terminates(lines))

def terminates(lines):
    visited = set()
    n = 0
    acc = 0
    while True:
        if n in visited:
            return False, acc
        if n == len(lines):
            return True, acc
        visited.add(n)
        instr,  num = lines[n]
        if instr == 'acc':
            acc += num
            n += 1
        elif instr == 'jmp':
            n += num
        elif instr == 'nop':
            n += 1


solve(open('test.txt').read())
solve(open('real.txt').read())
