# ref: https://blog.naver.com/mym0404/222323009491
import collections

N = int(input())
dp = collections.defaultdict(int)
dp[1] = 1
for i in range(1, N):
    if dp[i+1] < dp[i] + 1:
        dp[i+1] = dp[i] + 1
    for j in range(3):
        if dp[i + 3 + j] < dp[i] * (2 + j):
            dp[i + 3 + j] = dp[i] * (2 + j)

print(dp[N])