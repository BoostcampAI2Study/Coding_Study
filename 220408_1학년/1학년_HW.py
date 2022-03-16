import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().strip().split()))
dp = [[0] * 21 for _ in range(N)]
dp[0][num_list[0]] = 1

for i in range(1, N - 1):
    for j in range(21):
        if dp[i - 1][j] > 0:
            if 0 <= j + num_list[i] <= 20:
                dp[i][j + num_list[i]] += dp[i - 1][j]
            if 0 <= j - num_list[i] <= 20:
                dp[i][j - num_list[i]] += dp[i - 1][j]

print(dp[N - 2][num_list[N - 1]])
