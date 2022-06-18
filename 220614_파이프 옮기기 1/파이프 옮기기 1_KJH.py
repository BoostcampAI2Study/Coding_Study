# https://www.acmicpc.net/problem/17070

import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]  # 가로, 세로, 대각선

dp[0][1][0] = 1
for r in range(N):
    for c in range(N):
        if board[r][c]:
            continue
        if 0 <= r - 1:
            dp[r][c][1] += dp[r - 1][c][1] + dp[r - 1][c][2]
        if 0 <= c - 1:
            dp[r][c][0] += dp[r][c - 1][0] + dp[r][c - 1][2]
        if 0 <= r - 1 and 0 <= c - 1:
            if not (board[r - 1][c] or board[r][c - 1]):
                dp[r][c][2] += (
                    dp[r - 1][c - 1][0] + dp[r - 1][c - 1][1] + dp[r - 1][c - 1][2]
                )
print(sum(dp[N - 1][N - 1]))
