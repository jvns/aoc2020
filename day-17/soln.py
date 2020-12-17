import sys
import numpy as np

N = 23


def neighbors(matrix, a, b, c):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                if i == 0 and j == 0 and k == 0:
                    continue
                if a+i < 0 or b+j < 0 or c+k < 0:
                    continue
                if a+i > N-1 or b+j > N-1 or c+k > N-1:
                    continue
                yield matrix[a+i][b+j][c+k]

def part1(input):
    matrix = np.zeros((N, N, N))
    for i, line in enumerate(input.split()):
        for j, c in enumerate(line):
            if c == '#':
                matrix[8][i+8][j+8] = 1
    for _ in range(6):
        new = np.copy(matrix)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    total = sum(neighbors(matrix, i, j, k))
                    if matrix[i][j][k] == 1 and total not in [2,3]:
                        new[i][j][k] = 0
                    if matrix[i][j][k] == 0 and total == 3:
                        new[i][j][k] = 1
        matrix = new
        #print(matrix)
        #print("============")
    print(np.sum(matrix))

    pass


part1(sys.stdin.read().strip())
