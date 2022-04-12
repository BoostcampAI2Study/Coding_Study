# https://www.acmicpc.net/problem/1495

import sys

input = sys.stdin.readline


N, S, M = map(int, input().split())  # S : 시작 볼륨, M : 볼륨 최댓값
V = list(map(int, input().split()))
answer = -1  # 마지막 곡의 최댓값
V_MAX = max(V)

dp = [set() for _ in range(N + 1)]


def dfs(index, volume):
    global answer, V_MAX, M
    if volume < 0 or M < volume:
        return
    if index == len(V):
        answer = max(answer, volume)
        return
    if (
        volume + (len(V) - index) * V_MAX < M
        and volume + (len(V) - index) * V_MAX < answer
    ):
        return
    dp[index].add(volume)
    if volume + V[index] not in dp[index + 1]:
        dfs(index + 1, volume + V[index])
    if volume - V[index] not in dp[index + 1]:
        dfs(index + 1, volume - V[index])


dfs(0, S)
print(answer)
