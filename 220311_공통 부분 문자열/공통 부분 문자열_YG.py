import sys

input = sys.stdin.readline

s1 = list(input().rstrip())
s2 = list(input().rstrip())

dp = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]

answer = 0

for idx1, c1 in enumerate(s1):
    for idx2, c2 in enumerate(s2):
        if c1 == c2:
            dp[idx2+1][idx1+1] = dp[idx2][idx1]+1

            answer = max(answer, dp[idx2+1][idx1+1])

print(answer)