from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int,input().rstrip())) for _ in range(N)]

visited = [[[1e9,1e9] for _ in range(M)] for _ in range(N)]

visited[0][0][0] = 1

dx = [0,1,0,-1]
dy = [1,0,-1,0]

q = deque()

q.append((0, 0, 0))

while q:
    x, y ,cnt = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0 and visited[nx][ny][cnt] == 1e9:
                visited[nx][ny][cnt] = visited[x][y][cnt]+1
                q.append((nx, ny, cnt))
            elif arr[nx][ny] == 1 and cnt == 0 and visited[nx][ny][cnt+1] == 1e9:
                visited[nx][ny][cnt+1] = visited[x][y][cnt]+1
                q.append((nx, ny, cnt+1))

answer = min(visited[N-1][M-1])
if answer == 1e9:
    print(-1)
else:
    print(answer)