import sys

def dfs(k):
    if dp[k] == k:
        return k
    return dfs(dp[k])

R, C = map(int, sys.stdin.readline().split())
BOARD = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

NR, NC = [0, 0, 1, -1, 1, -1, 1, -1], [1, -1, 0, 0, -1, -1, 1, 1]
dp = [-1] * (R * C)
ball_board = [[0] * C for _ in range(R)]

for r in range(R):
    for c in range(C):
        min_r, min_c = r, c
        for i in range(8):
            nr, nc = r + NR[i], c + NC[i]
            a = BOARD[min_r][min_c]
            if 0 <= nr < R and 0 <= nc < C and BOARD[r][c] > BOARD[nr][nc] and BOARD[min_r][min_c] > BOARD[nr][nc]:
                min_r, min_c = nr, nc
        dp[C * r + c] = C * min_r + min_c

for i in range(R * C):
    dp[i] = dfs(i)
    ball_board[dp[i] // C][dp[i] % C] += 1

for i in range(R):
    print(' '.join(list(map(str, ball_board[i]))))
