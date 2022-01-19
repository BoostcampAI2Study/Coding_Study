N, M, K = map(int, input().split())

MAP = []
for _ in range(N):
    MAP.append(list(map(int, input())))

from collections import deque

q = deque([(0,0,K)])
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
ans = -1

while q:
    r, c, k = q.popleft()

    for dr, dc in (-1,0), (0,1), (1, 0), (0,-1):
        nr, nc = r+dr, c+dc

        if 0<=nr<N and 0<=nc<M:
            if visited[nr][nc]:
                continue
            if MAP[nr][nc] == 1:
                if k == 0:
                    continue
                k-=1
            q.append((nr, nc, k))
            visited[nr][nc] = visited[r][c] + 1

print(visited)
if visited[N-1][M-1] == 0:
    print(-1)
else:
    print(visited[N-1][M-1])
