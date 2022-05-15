import sys
sys.setrecursionlimit(10 ** 6)

def dfs(r, c):
    if not visit[r][c]:
        visit[r][c] = -1
        nr, nc = directions[MAP[r][c]][0] + r, directions[MAP[r][c]][1] + c
        if 0 <= nr < N and 0 <= nc < M:
            visit[r][c] = dfs(nr, nc)
        else:
            visit[r][c] = 1
            return 1
    return visit[r][c]

N, M = map(int, sys.stdin.readline().split())
MAP = [sys.stdin.readline() for _ in range(N)]

directions = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
visit = [[0] * M for _ in range(N)]
cnt = 0
for r in range(N):
    for c in range(M):
        if (not visit[r][c] and dfs(r, c) == 1) or visit[r][c] == 1:
            cnt += 1
print(cnt)
