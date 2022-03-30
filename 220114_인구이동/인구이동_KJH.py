# https://www.acmicpc.net/problem/16234

from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline

N, L, R = map(int, input().split())

# 연합이 되면 각 칸의 인구수는 평균이 된다.
nations = []
for _ in range(N):
    nations.append(list(map(int, input().split())))


def bfs(start: tuple):
    global L, R
    acc_num = cnt = 0
    q = deque([start])
    while q:
        x, y = q.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = 1
        visited_set.add((x, y))
        acc_num += nations[x][y]
        cnt += 1
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= x + dx < N and 0 <= y + dy < N and not visited[x + dx][y + dy]:
                if L <= abs(nations[x][y] - nations[x + dx][y + dy]) <= R:
                    q.append((x + dx, y + dy))
    return acc_num // cnt


answer = 1

all_nation = set([(i, j) for i in range(N) for j in range(N)])
for i in range(2001):
    tmp_set = set()
    visited = [[0 for _ in range(N)] for _ in range(N)]
    update = end = False
    if i == 0:
        left_nation = deepcopy(all_nation)
    while left_nation:
        visited_set = set()
        start = left_nation.pop()
        population = bfs(start)
        if len(visited_set) > 1:
            update = True
            if len(visited_set) == N * N:
                end = True
                break
            tmp_set |= visited_set
            for x, y in visited_set:
                nations[x][y] = population
        left_nation -= visited_set
    left_nation = deepcopy(tmp_set)
    if update:
        if end:
            print(answer)
            break
        else:
            answer += 1
    else:
        print(answer - 1)
        break
