def number(desc):
    a, *b = desc.split()
    return (a, ' '.join(b))
def parse(line):
    src, dest = line.split('contain')
    src = src.replace('bags', '').replace('bag', '').strip()
    if 'no other' in dest:
        dest = []
    else:
        dest = dest.replace('.', '').split(',')
        dest = [b.replace('bags', '').replace('bag', '').strip() for b in dest]
        dest = list(map(number, dest))
    #print(src, dest)
    return(src, dest)

from collections import defaultdict
def make_graph(parsed):
    d = defaultdict(list)
    for src, dest in parsed:
        for da in dest:
            num, x = da
            d[x].append(src)
    return d

def bfs(graph):
    found = set()
    queue = ['shiny gold']
    while len(queue) > 0:
        x = queue.pop()
        for t in graph[x]:
            if t not in found:
                queue.append(t)
                found.add(t)
    return found


def calc_num(bag_type, data):
    return sum(int(num) * calc_num(typ, data) for num, typ in data[bag_type]) + 1

def solve(input):
    lines = input.strip().split("\n")
    parsed = [parse(l) for l in lines]
    print("part 1")
    print(len(bfs(make_graph(parsed))))

    print("part 2")
    parsed = dict(parsed)
    print(calc_num('shiny gold', parsed) - 1)



solve(open('test.txt').read())
solve(open('real.txt').read())
