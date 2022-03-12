import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())

graph = []
for _ in range(N):
    sub = list(map(int, input().rstrip()))
    graph.append(sub)

distance = [[[]] * M for _ in range(N)]
for a in range(N):
    for b in range(M):
        distance[a][b] = [1e9]*(K+1)

# 초기화
distance[0][0][0] = 1

# 이동
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# bfs를 활용하여 거리 계산및 업데이트
q = deque()

# x, y, 벽부순 횟수
q.append((0, 0, 0))

while q:
    x, y, cnt = q.popleft()

    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]

        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0:
                if distance[nx][ny][cnt] > distance[x][y][cnt]+1:
                    q.append((nx, ny, cnt))
                    distance[nx][ny][cnt] = distance[x][y][cnt]+1
            else:
                if cnt >= K:
                    continue

                # 낮인 경우
                if distance[x][y][cnt] % 2 == 1:
                    if distance[nx][ny][cnt+1] > distance[x][y][cnt]+1:
                        q.append((nx, ny, cnt+1))
                        distance[nx][ny][cnt+1] = distance[x][y][cnt]+1
                # 밤인 경우
                else:
                    if distance[nx][ny][cnt+1] > distance[x][y][cnt]+2:
                        q.append((nx, ny, cnt+1))
                        distance[nx][ny][cnt+1] = distance[x][y][cnt]+2

answer = min(distance[N-1][M-1])

if answer == 1e9:
    print(-1)
else:
    print(answer)