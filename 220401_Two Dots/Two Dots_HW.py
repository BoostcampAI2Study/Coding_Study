import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
NR = [0, 0, 1, -1]
NC = [1, -1, 0, 0]

def dfs(r, c, color, start, dot_cnt):
    # check cycle
    if dot_cnt >= 3 and start[0] == r and start[1] == c:
        print("Yes")
        sys.exit()
    # move
    for i in range(4):
        nr, nc = NR[i] + r, NC[i] + c
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == color and not visit[nr][nc]:
            visit[nr][nc] = True
            dfs(nr, nc, color, start, dot_cnt + 1)
            visit[nr][nc] = False

for r in range(N):
    for c in range(M):
        if not visit[r][c]:
            dfs(r, c, board[r][c], (r, c), 0)
            visit[r][c] = True
print("No")
