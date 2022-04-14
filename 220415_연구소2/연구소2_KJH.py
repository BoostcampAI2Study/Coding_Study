# https://www.acmicpc.net/problem/17141

from collections import deque
import sys

from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())  # 연구소 크기, 바이러스 개수
lab = []
virus_pos = []
for i in range(N):
    lab.append(list(map(int, input().split())))
    for j in range(N):
        if lab[-1][j] == 2:
            virus_pos.append((i, j))

candi_virus = combinations(virus_pos, M)

min_time = float("inf")


def bfs(viruses):
    max_cnt = 0
    q = []
    for pos in viruses:
        q.append((pos, 0))
    q = deque(q)
    while q:
        node, cnt = q.popleft()
        x, y = node
        if visited[x][y] != -1:
            continue
        visited[x][y] = cnt
        max_cnt = max(max_cnt, cnt)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if lab[nx][ny] != 1 and visited[nx][ny] == -1:
                    q.append(((nx, ny), cnt + 1))
    return max_cnt


for virus_pos in candi_virus:
    visited = [[-1] * N for _ in range(N)]
    cnt = bfs(virus_pos)
    if min_time > cnt:
        exist_blank = False
        for i in range(N):
            for j in range(N):
                if visited[i][j] == -1 and lab[i][j] != 1:
                    exist_blank = True
                    break
            if exist_blank:
                break
        else:
            min_time = cnt
print(min_time if min_time != float("inf") else -1)
