import sys, collections
N = int(sys.stdin.readline())
BOARD = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cur_r, cur_c = 0, 0
for r in range(N):
    for c in range(N):
        if BOARD[r][c] == 1:
            cur_r, cur_c = r, c

result = 1e9
q = collections.deque()
visit = [[[[False] * 3 for _ in range(N ** 2 + 1)] for _ in range(N)] for _ in range(N)]
for direction in range(3):
    q.append((cur_r, cur_c, direction, 0, 2))
    visit[cur_r][cur_c][2][direction] = True

while q:
    r, c, d, t, goal = q.popleft()
    if BOARD[r][c] == N ** 2 and goal == N ** 2:
        result = min(result, t)
        continue

    if BOARD[r][c] == goal:
        goal += 1
        visit[r][c][goal][d] = True
    
    # change chess piece
    for direction in range(3):
        if direction != d and not visit[r][c][goal][direction]:
            q.append((r, c, direction, t + 1, goal))
            visit[r][c][goal][direction] = True

    # knight
    if d == 0:
        for nr, nc in [(-2, -1), (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2)]:
            nr, nc = nr + r, nc + c
            if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc][goal][d]:
                q.append((nr, nc, 0, t + 1, goal))
                visit[nr][nc][goal][d] = True
    # bishop
    elif d == 1:
        for s in range(1, N + 1):
            for nr, nc in [(-s, -s), (-s, s), (s, -s), (s, s)]:
                nr, nc = nr + r, nc + c
                if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc][goal][d]:
                    q.append((nr, nc, 1, t + 1, goal))
                    visit[nr][nc][goal][d] = True
    # rook
    elif d == 2:
        for s in range(1, N + 1):
            for nr, nc in [(0, s), (0, -s), (s, 0), (-s, 0)]:
                nr, nc = nr + r, nc + c
                if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc][goal][d]:
                    q.append((nr, nc, 2, t + 1, goal))
                    visit[nr][nc][goal][d] = True

print(result)
