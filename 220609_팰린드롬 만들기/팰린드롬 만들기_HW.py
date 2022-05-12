# ref:https://ddiyeon.tistory.com/67 (LCS 사용)
import sys
N = int(sys.stdin.readline())
SEQUENCE = list(map(int, sys.stdin.readline().split()))

dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if SEQUENCE[i - 1] == SEQUENCE[-j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(N - dp[N][N])
