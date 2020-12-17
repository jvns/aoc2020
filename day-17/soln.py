import sys
import numpy as np

N = 23


def neighbors(matrix, a, b, c, d):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    if i == 0 and j == 0 and k == 0 and l == 0:
                        continue
                    if a+i < 0 or b+j < 0 or c+k < 0 or d + l < 0:
                        continue
                    if a+i > N-1 or b+j > N-1 or c+k > N-1 or d + l > N-1:
                        continue
                    yield matrix[a+i][b+j][c+k][d+l]

def part1(input):
    matrix = np.zeros((N, N, N, N))
    for i, line in enumerate(input.split()):
        for j, c in enumerate(line):
            if c == '#':
                matrix[8][i+8][j+8][8] = 1
    for _ in range(6):
        print('did an iteration')
        new = np.copy(matrix)
        where = np.where(matrix > 0)
        max_i, max_j, max_k, max_l = [np.max(x) for x in where]
        min_i, min_j, min_k, min_l = [np.min(x) for x in where]
        for i in range(min_i-1, max_i+2):
            for j in range(min_j-1, max_j+2):
                for k in range(min_k-1, max_k+2):
                    for l in range(min_l-1, max_l+2):
                        total = sum(neighbors(matrix, i, j, k, l))
                        if matrix[i][j][k][l] == 1 and total not in [2,3]:
                            new[i][j][k][l] = 0
                        if matrix[i][j][k][l] == 0 and total == 3:
                            new[i][j][k][l] = 1
        matrix = new
    print(np.sum(matrix))

    pass


part1(sys.stdin.read().strip())
