import collections

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

NR = [0, 0, 1, -1, 1, 1, -1, -1]
NC = [1, -1, 0, 0, 1, -1, 1, -1]

def bfs(loc):
    safe_distances = [[-1] * M for _ in range(N)]
    q = collections.deque()
    q.append(loc)
    safe_distances[loc[0]][loc[1]] = 0

    while q:
        r, c = q.popleft()
        for i in range(8):
            nr, nc = r + NR[i], c + NC[i]
            if 0 <= nr < N and 0 <= nc < M and safe_distances[nr][nc] == -1:
                if board[nr][nc] == 1:
                    return safe_distances[r][c] + 1
                else:
                    q.append((nr, nc))
                    safe_distances[nr][nc] = safe_distances[r][c] + 1
result = -1
for r in range(N):
    for c in range(M):
        # board = 0 인 부분에서 가장 가까운 상어와의 안전 거리 계산
        if board[r][c] == 0:
            result = max(result, bfs((r,c)))
print(result)
