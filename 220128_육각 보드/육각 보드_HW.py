import sys
sys.setrecursionlimit(10**6)

N = int(input())
board = [list(input()) for _ in range(N)]
visit = [[False] * N for _ in range(N)]
result = -1

for r in range(N):
    for c in range(N):
        if board[r][c] == "X":
            board[r][c] = 0
        else:
            board[r][c] = -1

def dfs(r, c, color):
    global result
    visit[r][c] = True
    for nr, nc in [(-1, 0), (0, -1), (1, -1), (1, 0), (0, 1), (-1, 1)]:
        nr, nc = r + nr, c + nc
        if nr < 0 or nc < 0 or nr >= N or nc >= N:
            continue
        if visit[nr][nc] == True:
            if board[nr][nc] == color:
                result = 3
                return
            else:
                continue

        if board[nr][nc] == -1:
            if result < color:
                result = color
        else:
            if color == 1:
                board[nr][nc] = 2
                dfs(nr, nc, 2)
            else:
                board[nr][nc] = 1
                dfs(nr, nc, 1)

for r in range(N):
    for c in range(N):
        if board[r][c] == 0 and visit[r][c] is False:
            board[r][c] = 1
            dfs(r, c, 1)

if N == 1 and board[0][0] == 1:
    print(1)
else:
    print(result) if result != -1 else print(0)