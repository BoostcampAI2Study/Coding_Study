import sys
from collections import defaultdict
input = sys.stdin.readline

# Input
N, K = map(int, input().split())

db = [[0,0]]
for _ in range(N):
    W, V = map(int, input().split())
    db.append([W,V])

# 최대 무게별 최대 가치?
dp = [[0]*(K+1) for _ in range(N+1)]

# dp[x][y] -> x=몇번째까지?, y = 무게
for x in range(1, N+1):
    for y in range(1, K+1):
        if db[x][0] > y:
            dp[x][y] = dp[x-1][y]
        else:
            dp[x][y] = max(dp[x-1][y], dp[x-1][y-db[x][0]]+db[x][1])

print(dp[N][K])