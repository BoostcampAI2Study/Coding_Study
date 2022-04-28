
from collections import deque
from copy import deepcopy
from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
LAB = []
VIRUS_POS = []
BLANK_NUM = 0
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 2:
            VIRUS_POS.append((i, j))
    LAB.append(line)
    BLANK_NUM += line.count(0)


def bfs(virus_pos, visited):
    global BLANK_NUM
    cnt = 0
    max_time = 0
    dp = [[float("inf")] * N for _ in range(N)]
    q = deque([[(x, y), 0] for x, y in virus_pos])
    while q:
        (x, y), time = q.popleft()
        if visited[x][y] == 1 or dp[x][y] <= time:
            continue
        max_time = max(max_time, time)
        if visited[x][y] != 2:
            cnt += 1
            dp[x][y] = time
        visited[x][y] = 1

        if cnt == BLANK_NUM:
            return max_time
        for dx, dy in [(0, 1), (-1, 0), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] != 1:
                    q.append([(nx, ny), time + 1])
    return -1


answer = float("inf")
for virus in combinations(VIRUS_POS, M):
    max_time = bfs(virus, deepcopy(LAB))
    if max_time != -1:
        answer = min(answer, max_time)

print(answer if answer != float("inf") else -1)
