import collections

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
visit = [[0] * N for _ in range(N)]
NR = [-2, -2, 0, 0, 2, 2]
NC = [-1, 1, -2, 2, -1, 1]

q = collections.deque()
q.append((r1, c1))
while q:
    r, c = q.popleft()
    if r == r2 and c == c2:
        break
    for i in range(6):
        nr, nc = r + NR[i], c + NC[i]
        if nr < 0 or nc < 0 or nr >= N or nc >= N or visit[nr][nc] != 0:
            continue

        q.append((nr, nc))
        visit[nr][nc] = visit[r][c] + 1

print(visit[r2][c2]) if visit[r2][c2] != 0 else print(-1)