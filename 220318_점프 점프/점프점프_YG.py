import sys
from collections import deque
input = sys.stdin.readline

# Input
N = int(input())
miro = list(map(int, input().split()))

# Initialization
dp = [1e9]*(N)
dp[0] = 0

# Dp
for i in range(N):
    for k in range(miro[i]+1):
        if i+k < N:
            dp[i+k] = min(dp[i+k], dp[i]+1)

# Output
if dp[N-1] == 1e9:
    print(-1)
else:
    print(dp[N-1])



