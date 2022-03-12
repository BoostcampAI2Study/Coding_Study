import sys
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split())

gonggan = [list(map(int, input().split())) for _ in range(N)]

distances = [[1e9]*M for _ in range(N)]

dx = [0,1,0,-1,-1,1,1,-1]
dy = [1,0,-1,0,1,1,-1,-1]

for a in range(N):
    for b in range(M):
        if gonggan[a][b] == 1:
            q = deque()

            q.append((a, b))

            distances[a][b] = 0

            while q:
                x, y = q.popleft()
                for k in range(8):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if distances[nx][ny] > distances[x][y]+1 and gonggan[nx][ny] == 0:
                            distances[nx][ny] = distances[x][y]+1
                            q.append((nx, ny))

print(max(map(max,distances)))