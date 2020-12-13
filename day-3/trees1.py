import sys
with open(sys.argv[1]) as f:
    trees = [x.strip() for x in f.readlines()]

def tree_count(right, down):
    x = 0
    y = 0
    width = len(trees[0])
    tree_count = 0
    while y < len(trees):
        if trees[y][x] == '#':
            tree_count += 1
        x = (x + right) % width
        y += down
    return tree_count

print(tree_count(1,1) )
print(tree_count(3,1) )
print(tree_count(5,1) )
print(tree_count(7,1) )
print(tree_count(1,2))
print(tree_count(1,1) * tree_count(3,1) * tree_count(5,1) * tree_count(7,1) * tree_count(1,2))
