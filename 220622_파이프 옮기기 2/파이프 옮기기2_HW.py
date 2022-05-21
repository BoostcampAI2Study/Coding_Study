import sys
N = int(sys.stdin.readline())
HOUSE = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[[0] * N for _ in range(N)] for _ in range(3)] # 가로 세로 대각선

dp[0][0][1] = 1
for r in range(N):
    for c in range(2, N):
        if not HOUSE[r][c]:
            dp[0][r][c] = dp[0][r][c - 1] + dp[2][r][c - 1]
            dp[1][r][c] = dp[1][r - 1][c] + dp[2][r - 1][c]
            if not HOUSE[r - 1][c] and not HOUSE[r][c - 1]:
                dp[2][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]
print(dp[0][N - 1][N - 1] + dp[1][N - 1][N - 1] + dp[2][N - 1][N - 1])
