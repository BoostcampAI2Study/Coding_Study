# https://www.acmicpc.net/problem/16929

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

table = [input().strip() for _ in range(N)]

answer = False

visited = [[False] * M for _ in range(N)]


def dfs(now, prev, color):
    global answer

    x, y = now
    visited[x][y] = True
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= x + dx < N and 0 <= y + dy < M:
            if not visited[x + dx][y + dy]:
                if table[x + dx][y + dy] == color:
                    if dfs((x + dx, y + dy), now, color):
                        return True
            else:
                if table[x + dx][y + dy] == color and (x + dx, y + dy) != prev:
                    return True
    return False


for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            if dfs((i, j), (i, j), table[i][j]):
                print("Yes")
                sys.exit()
print("No")
