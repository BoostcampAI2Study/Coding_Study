import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())


table = []
blank = []
virus = []
for i in range(N):
    line = list(map(int, input().split()))
    for j, n in enumerate(line):
        if n == 0:
            blank.append((i, j))
        elif n == 2:
            virus.append((i, j))
    table.append(line)

answer = -1
candi = list(combinations(blank, 3))
cnt = len(blank) - 3


def dfs(c, r):
    global cnt
    if test_table[c][r] == 0:
        test_table[c][r] = 2

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= c + dx < N and 0 <= r + dy < M and test_table[c + dx][r + dy] == 0:
            cnt -= 1
            dfs(c + dx, r + dy)


for test_blank in candi:
    cnt = len(blank) - 3
    test_table = [i[:] for i in table]
    for x, y in test_blank:
        test_table[x][y] = 1
    for v in virus:
        dfs(v[0], v[1])
    answer = max(answer, cnt)
print(answer)
