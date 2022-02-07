import sys

input = sys.stdin.readline

N = int(input())

# 스크린
dp = [0]*(N+1)

# 1번
for k in range(1, N+1):
    dp[k] = k

# for 문
for i in range(7, N+1):
    for j in range(1, i-2):
        dp[i] = max(dp[i], dp[j]*(i-j-1))

print(dp[N])
