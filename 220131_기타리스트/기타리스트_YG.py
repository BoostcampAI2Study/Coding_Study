import sys

input = sys.stdin.readline

# N = 곡의 개수, S = 시작 볼륨, M = 최대 볼륨
N, S, M = map(int, input().split())

# 볼륨 리스트
V = list(map(int, input().split()))


ans = [[False]*(M+1) for _ in range(N+1)]

ans[0][S] = True

for song in range(N):
    for volume in range(M+1):
        if ans[song][volume] == True:
            for next_volume in [volume+V[song], volume-V[song]]:
                if 0 <= next_volume <= M:
                    ans[song+1][next_volume] = True


answer = -1

for k in range(M+1):
    if ans[N][k] == True:
        answer = max(answer, k)

print(answer)