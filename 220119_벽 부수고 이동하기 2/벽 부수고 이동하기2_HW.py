import collections

n, m, k = map(int, input().split())
board = [list(map(int, input())) for j in range(n)]
visited = [[[0] * (k+1) for _ in range(m)] for j in range(n)]

q = collections.deque()
q.append((0, 0, k))
visited[0][0][k] = 1

while q:
    x, y, nk = q.popleft()

    for nx, ny in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        nx, ny = nx + x, ny + y
        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny][nk] != 0:
            continue
        if nk > 0 and board[nx][ny] == 1:
            q.append((nx, ny, nk - 1))
            visited[nx][ny][nk - 1] = visited[x][y][nk] + 1
        elif board[nx][ny] == 0:
            q.append((nx, ny, nk))
            visited[nx][ny][nk] = visited[x][y][nk] + 1

result = 1e9
for i in visited[n - 1][m - 1]:
    if 0 < i < result:
        result = i
print(result) if result != 1e9 else print(-1)