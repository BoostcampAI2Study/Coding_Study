import sys
from collections import deque
input = sys.stdin.readline

# Input
N, M = map(int,input().split())

graph = [list(map(int,list(input().rstrip()))) for _ in range(N)]

answer = [[0]*M for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

visited = set()
for x in range(N):
    for y in range(M):
        if graph[x][y] == 1:
            answer[x][y] += 1
            continue
        if (x,y) in visited:
            continue

        visited2 = set()
        visited.add((x, y))
        for i in range(4):
            mx, my = x + dx[i], y + dy[i]
            if 0 <= mx < N and 0 <= my < M:
                visited2.add((mx, my))
        q = deque()

        cnt = 1

        q.append((x, y))

        while q:
            nx, ny = q.popleft()
            for k in range(4):
                nnx, nny = nx+dx[k], ny+dy[k]
                if 0 <= nnx < N and 0 <= nny < M and graph[nnx][nny] == 0 and not (nnx,nny) in visited:
                    visited.add((nnx, nny))

                    for p in range(4):
                        nnnx, nnny = nnx+dx[p], nny+dy[p]
                        if 0 <= nnnx < N and 0 <= nnny < M:
                            visited2.add((nnnx, nnny))
                    q.append((nnx, nny))
                    cnt += 1
        for xx, yy in visited2:
            if graph[xx][yy] == 1:
                answer[xx][yy] += cnt

for a in range(N):
    for b in range(M):
        answer[a][b] %= 10

for a in answer:
    print("".join(map(str, a)))
