N, M, K = map(int, input().split())

MAP = []
for _ in range(N):
    MAP.append(list(map(int, input())))

from collections import deque

q = deque([(0,0,0)])
visited = [[[1e9]*M for _ in range(N)] for _ in range(K+1)]

for i in range(K+1):
    visited[i][0][0] = 1
while q:
    r, c, k = q.popleft()

    for dr, dc in (-1,0), (0,1), (1, 0), (0,-1):
        nr, nc = r+dr, c+dc
        
        if 0<=nr<N and 0<=nc<M:
            if visited[k][nr][nc] != 1e9:
                continue

            if MAP[nr][nc] == 0:
                visited[k][nr][nc] = visited[k][r][c] + 1
                q.append((nr, nc, k))
                
            elif MAP[nr][nc] == 1:
                if k == K:
                    continue
                visited[k+1][nr][nc] = min(visited[k][r][c] + 1, visited[k+1][nr][nc])
                q.append((nr, nc, k+1))


# for matrix in visited:
#     for r in matrix:
#         print(r)
#     print()

ans = 1e9
for i in range(K+1):
    ans = min(ans, visited[i][N-1][M-1])

print(ans if ans != 1e9 else -1)
