import collections

n, m, k = map(int, input().split())
board = [list(map(int, input())) for j in range(n)]
visited = [[[0] * (k+1) for _ in range(m)] for j in range(n)]

q = collections.deque()
q.append((0, 0, k))
visited[0][0][k] = 1
result = -1

while q:
    r, c, nk = q.popleft()
    if r == n-1 and c == m-1:
        result = visited[r][c][nk]
        break
    for nr, nc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        nr, nc = nr + r, nc + c
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        if nk > 0 and board[nr][nc] == 1 and visited[nr][nc][nk - 1] == 0:
            q.append((nr, nc, nk - 1))
            visited[nr][nc][nk - 1] = visited[r][c][nk] + 1
        elif board[nr][nc] == 0 and visited[nr][nc][nk] == 0:
            q.append((nr, nc, nk))
            visited[nr][nc][nk] = visited[r][c][nk] + 1

print(result)
