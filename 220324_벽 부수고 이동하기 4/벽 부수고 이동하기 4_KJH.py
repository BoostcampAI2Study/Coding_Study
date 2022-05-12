# https://www.acmicpc.net/problem/16946

from collections import defaultdict, deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
MAP = [list(input().strip()) for _ in range(N)]

mapping = defaultdict(int)


def bfs(x, y):
    global N, M, MAP, mapping
    q = deque([(x, y)])
    cnt = 0
    MAP[x][y] = -1
    while q:
        r, c = q.popleft()
        cnt += 1
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if MAP[nr][nc] == "0":
                    MAP[nr][nc] = -1
                    q.append((nr, nc))
    q = deque([(x, y)])

    MAP[x][y] = len(mapping)
    while q:
        r, c = q.popleft()
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if MAP[nr][nc] == -1:
                    MAP[nr][nc] = len(mapping)
                    q.append((nr, nc))
    mapping[len(mapping)] = cnt


NEW_MAP = [["0"] * M for _ in range(N)]

for r in range(N):
    for c in range(M):
        if MAP[r][c] == "0":
            bfs(r, c)
for r in range(N):
    for c in range(M):
        if MAP[r][c] == "1":
            tmp = set()
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M:
                    if MAP[nr][nc] != "1":
                        tmp.add(MAP[nr][nc])
            NEW_MAP[r][c] = str((sum(list(map(lambda x: mapping[x], tmp))) + 1) % 10)
for line in NEW_MAP:
    print("".join(line))
