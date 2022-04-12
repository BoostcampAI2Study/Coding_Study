# https://www.acmicpc.net/problem/12946

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
board = [list(input().strip()) for _ in range(N)]
X_CNT = sum(map(lambda x: x.count("X"), board))

dxdy = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]

visited_color = [[0] * N for _ in range(N)]

# 최대 3가지 색만 쓸 수 있다.
def dfs(node):
    global min_color
    x, y = node
    min_color = max(min_color, 1)
    for dx, dy in dxdy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == "X":
            if visited_color[nx][ny] == visited_color[x][y]:
                print(3)
                sys.exit()
            elif not visited_color[nx][ny]:
                visited_color[nx][ny] = 3 - visited_color[x][y]
                min_color = max(min_color, 2)
                dfs((nx, ny))


min_color = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == "X" and not visited_color[i][j]:
            exist_X = True
            visited_color[i][j] = 1
            dfs((i, j))

print(min_color)
