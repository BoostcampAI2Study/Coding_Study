import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
BACKPACKS = [(0, 0)] + [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dp = [[0]*(K+1) for _ in range(N+1)]
for bag_idx in range(1, N+1):
    bag_weight, bag_value = BACKPACKS[bag_idx]
    for weight in range(1, K+1):
        if weight < bag_weight:
            dp[bag_idx][weight] = dp[bag_idx-1][weight]
        else:
            dp[bag_idx][weight] = max(dp[bag_idx-1][weight-bag_weight] + bag_value, dp[bag_idx-1][weight])

print(dp[N][K])