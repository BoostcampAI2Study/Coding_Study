# ref: https://velog.io/@turtle601/백준-행렬-곱셈-순서-11049번
import sys
N = int(sys.stdin.readline())
MATRIX = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for i in range(1, N):
    for j in range(N - i):
        end = i + j
        dp[j][end] = 1e9
        for k in range(j, end):
            dp[j][i] = min(dp[j][end], dp[j][k] + dp[k + 1][end] + MATRIX[j][0] * MATRIX[k][1] * MATRIX[end][1])

print(dp[0][N-1])
