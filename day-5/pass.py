import sys
with open(sys.argv[1]) as f:
    lines = [x.strip() for x in f.readlines()]

def f():
    for l in lines:
        x = l[:7].replace('F', '0').replace('B', '1')
        y = l[-3:].replace('L', '0').replace('R', '1')
        row = int(x, 2)
        col = int(y, 2)
        print(row,col)
        yield (row * 8) + col

prev = 44
for x in (list(sorted((f())))):
    if x != prev+1:
        print(x)
    prev = x



print(list(sorted(f())))
