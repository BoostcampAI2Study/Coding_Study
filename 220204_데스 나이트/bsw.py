N = int(input())

r1, c1, r2, c2 = map(int, input().split())

move = [(-2, -1), (-2, 1), (0, -2), (0, 2), (+2, -1), (+2, +1)]

ans = 1e9

from collections import deque

q=deque()
q.append((r1,c1))
visited=[[-1 for _ in range(N)] for _ in range(N)]
visited[r1][c1] = 0

while q:
    r, c = q.popleft()

    for dr, dc in move:
        nr, nc = r+dr, c+dc

        if 0<=nr<N and 0<=nc<N:
            if visited[nr][nc] >= 0:
                continue
            visited[nr][nc] = visited[r][c] +1
            q.append((nr,nc))

print(visited[r2][c2])
# print(visited)

