# 연걸님 코드보고 공부했습니다.

N, S, M = map(int, input().split())
V = list(map(int, input().split()))

dp = [[False]*(M+1) for _ in range(N+1)]
dp[0][S] = True

for song in range(N):
    for volume in range(M+1):
        if dp[song][volume] == True:
            for next_volume in [volume+V[song], volume-V[song]]:
                if 0<=next_volume<=M:
                    dp[song+1][next_volume] = True
answer = -1
for volume in range(M, -1, -1):
    if dp[N][volume]==True:
        answer=volume
        break
print(answer)
