import collections
n, m, k = map(int, input().split())
board = [list(map(int, input())) for j in range(n)]
visited = [[[False] * m for _ in range(n)] for _ in range(k + 1)]
NR = [0, 0, 1, -1]
NC = [-1, 1, 0, 0]

q = collections.deque()
q.append((0, 0, k, 1, True))
visited[k][0][0] = True
result = -1

while q:
    r, c, nk, move = q.popleft()
    if r == n - 1 and c == m - 1:
        result = move
        break
    for i in range(4):
        nr, nc = NR[i] + r, NC[i] + c
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        if board[nr][nc] == 1:
            if nk > 0 and not visited[nk - 1][nr][nc]:
                if move % 2 != 0:
                    q.append((nr, nc, nk - 1, move + 1))
                    visited[nk - 1][nr][nc] = True
                else:
                    q.append((r, c, nk, move + 1))
        else:
            if not visited[nk][nr][nc]:
                q.append((nr, nc, nk, move + 1))
                visited[nk][nr][nc] = True

print(result)
