# https://www.acmicpc.net/problem/10026

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
table = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]


def dfs(node, is_RG=False):
    x, y = node
    if visited[x][y]:
        return
    visited[x][y] = 1

    if is_RG:
        if table[x][y] == "B":
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if not visited[nx][ny] and table[nx][ny] == "B":
                        dfs((nx, ny), is_RG)
        else:
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if not visited[nx][ny] and table[nx][ny] != "B":
                        dfs((nx, ny), is_RG)

    else:
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and table[nx][ny] == table[x][y]:
                    dfs((nx, ny), is_RG)


answer1 = 0
answer2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            answer1 += 1
            dfs((i, j))
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            answer2 += 1
            dfs((i, j), True)
print("{} {}".format(answer1, answer2))
