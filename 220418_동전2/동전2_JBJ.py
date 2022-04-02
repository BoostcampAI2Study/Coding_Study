import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
COINS = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

dp = [0] + [1e9]*K
for coin_value in COINS:
    for cur_total_value in range(1, K+1):
        if cur_total_value >= coin_value:
            dp[cur_total_value] = min(dp[cur_total_value] , dp[cur_total_value-coin_value]+1)

print(dp[-1] if dp[-1] != 1e9 else -1)