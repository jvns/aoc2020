import sys
import itertools

def part1(input):
    results = {}
    for line in input.split('\n'):
        print(line)
        if 'mask' in line:
            mask = line.split(' = ')[1]
        else:
            #mem[21836] = 68949
            fst, snd = line.split(' = ')
            idx, result = int(fst[4:-1]), int(snd)
            result = '{0:036b}'.format(result)
            results[idx] = int(''.join([r if m == 'X' else m for r, m in zip(result, mask)]), 2)

    print(sum(results.values()))

def weird_and(m, i):
    if m == 'X':
        return ['0', '1']
    if m == '1':
        return [m]
    return [i]

def addresses(mask, idx):
    sets = [weird_and(m, i) for m, i in zip(mask, idx)]
    return [int(''.join(x), 2) for x in itertools.product(*sets)]

def part2(input):
    results = {}
    for line in input.split('\n'):
        if 'mask' in line:
            mask = line.split(' = ')[1]
        else:
            #mem[21836] = 68949
            fst, snd = line.split(' = ')
            idx, result = int(fst[4:-1]), int(snd)
            idx = '{0:036b}'.format(idx)
            for addr in addresses(mask, idx):
                results[addr] = result

    print(sum(results.values()))


part2(sys.stdin.read().strip())
