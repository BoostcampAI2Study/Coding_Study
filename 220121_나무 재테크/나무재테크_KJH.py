# https://www.acmicpc.net/problem/16235

from copy import deepcopy
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
ROBOT = [list(map(int, input().split())) for _ in range(N)]
NUTRIENT = [[5] * N for _ in range(N)]
TREES = [[[] for _ in range(N)] for _ in range(N)]
DEATH_TREES = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    TREES[x - 1][y - 1].append(z)


def spring(node):
    x, y = node
    TREES[x][y].sort()
    tmp = []
    for idx, tree_old in enumerate(TREES[x][y]):
        if tree_old > NUTRIENT[x][y]:
            DEATH_TREES[x][y] = TREES[x][y][idx:]
            break
        NUTRIENT[x][y] -= tree_old
        tmp.append(tree_old + 1)
    TREES[x][y] = tmp[:]


def summer(node):
    x, y = node
    if DEATH_TREES[x][y]:
        for dead_tree in DEATH_TREES[x][y]:
            NUTRIENT[x][y] += dead_tree // 2
    DEATH_TREES[x][y] = []


def fall(node):
    x, y = node
    if TREES[x][y]:
        for tree in TREES[x][y]:
            if tree % 5 == 0:
                for dx, dy in [
                    (0, 1),
                    (0, -1),
                    (1, 0),
                    (-1, 0),
                    (1, 1),
                    (-1, 1),
                    (1, -1),
                    (-1, -1),
                ]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        TREES[nx][ny].append(1)


def winter(node):
    x, y = node
    NUTRIENT[x][y] += ROBOT[x][y]


for _ in range(K):
    for i in range(N):
        for j in range(N):
            if TREES[i][j]:
                spring((i, j))
                summer((i, j))
    for i in range(N):
        for j in range(N):
            if TREES[i][j]:
                fall((i, j))
            winter((i, j))
answer = 0

for line in TREES:
    answer += sum(map(len, line))
print(answer)
