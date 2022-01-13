import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().strip().split())
u = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cnt = 0

def bfs(r, c):
    q = deque()
    q.append((r, c))
    unites = []
    total = 0
    while q:
        x, y = q.popleft()
        total += u[x][y]
        unites.append((x, y))

        for dir in dirs:
            nx = x + dir[0]
            ny = y + dir[1]

            if 0 <= nx < N and 0 <= ny < N and not v[nx][ny]:
                if M <= abs(u[nx][ny] - u[x][y]) <= K:
                    v[nx][ny] = True
                    q.append((nx, ny))

    if len(unites) > 1:
        mean = total // len(unites)
        while unites:
            tmp_r, tmp_c = unites.pop()
            u[tmp_r][tmp_c] = mean
        return True
    return False

while True:
    flag = False
    v = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not v[i][j]:
                v[i][j] = True
                if bfs(i, j):
                    flag = True
    if not flag:
        break
    cnt += 1

print(cnt)
