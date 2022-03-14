import sys

input = sys.stdin.readline

N = int(input())

chillpan = list(input().split())

dp = [[0]*N for _ in range(N)]


for x in range(N):
    for y in range(N):
        if x == y:
            dp[x][y] = 1

for x in range(N):
    for y in range(N):
        if x+1 == y and chillpan[x] == chillpan[y]:
            dp[x][y] = 1

for k in range(2, N):
    for x in range(N - k):
        if chillpan[x] == chillpan[x+k] and dp[x+1][x+k-1] == 1:
            dp[x][x+k] = 1

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(dp[a-1][b-1])