import sys
sys.setrecursionlimit(10 ** 6)
N = int(input())
board = [list(input()) for _ in range(N)]

NR = [0, 0, 1, -1]
NC = [1, -1, 0, 0]
rgb_visit = [[False] * N for _ in range(N)]
gb_visit = [[False] * N for _ in range(N)]


def rgb_dfs(r, c, color):
    if board[r][c] != color:
        return
    rgb_visit[r][c] = True
    for i in range(4):
        nr, nc = r + NR[i], c + NC[i]
        if nr < 0 or nc < 0 or nr >= N or nc >= N or rgb_visit[nr][nc] is True:
            continue
        rgb_dfs(nr, nc, color)

def gb_dfs(r, c, color):
    if color == "R" or color == "G":
        if board[r][c] == "B":
            return
    elif color == "B":
        if board[r][c] == "R" or board[r][c] == "G":
            return
    gb_visit[r][c] = True
    for i in range(4):
        nr, nc = r + NR[i], c + NC[i]
        if nr < 0 or nc < 0 or nr >= N or nc >= N or gb_visit[nr][nc] is True:
            continue
        gb_dfs(nr, nc, color)

rgb_cnt = 0
gb_cnt = 0
for r in range(N):
    for c in range(N):
        if rgb_visit[r][c] is False:
            rgb_dfs(r, c, board[r][c])
            rgb_cnt += 1
        if gb_visit[r][c] is False:
            gb_dfs(r, c, board[r][c])
            gb_cnt += 1

print(rgb_cnt, gb_cnt)
