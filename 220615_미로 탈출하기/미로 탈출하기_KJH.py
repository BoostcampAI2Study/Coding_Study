# https://www.acmicpc.net/problem/17090

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())
maze = [list(input().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
direction = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}


def dfs(r, c):
    if not visited[r][c]:
        visited[r][c] = -1
        nr, nc = r + direction[maze[r][c]][0], c + direction[maze[r][c]][1]
        if 0 <= nr < N and 0 <= nc < M:
            visited[r][c] = dfs(nr, nc)
        else:
            visited[r][c] = 1
            return 1
    return visited[r][c]


answer = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 1 or dfs(i, j) == 1:
            answer += 1

print(answer)
