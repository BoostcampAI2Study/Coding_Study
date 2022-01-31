import sys
from collections import deque

input = sys.stdin.readline

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

N = int(input())

r1, c1, r2, c2 = map(int, input().split())

visited = [[False]*N for _ in range(N)]

visited[r1][c1] = True

q = deque()

q.append((r1, c1, 0))

while q:
    x, y, cnt = q.popleft()

    if x == r2 and y == c2:
        print(cnt)
        sys.exit()

    for k in range(6):
        nx, ny = x + dx[k], y + dy[k]

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
            visited[nx][ny] = True
            q.append((nx, ny, cnt+1))

print(-1)