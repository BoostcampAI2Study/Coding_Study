import sys
n, k = map(int, sys.stdin.readline().split())
coin_values = [int(sys.stdin.readline()) for _ in range(n)]
dp = [1e9] * (k + 1)
dp[0] = 0

for i in range(n):
    for value in range(coin_values[i], k + 1):
        dp[value] = min(dp[value], dp[value - coin_values[i]] + 1)
print(dp[k]) if dp[k] != 1e9 else print(-1)
