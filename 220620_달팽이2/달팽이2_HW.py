import sys
M, N = map(int, sys.stdin.readline().split())
directions = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

visit = [[False] * N for _ in range(M)]
r, c, d, cnt = 0, 0, 0, 0
while True:
    visit[r][c] = True
    nr, nc = r + directions[d][0], c + directions[d][1]
    if 0 <= nr < M and 0 <= nc < N and not visit[nr][nc]:
        r, c = nr, nc
    else:
        is_break = True
        for nd in range(4):
            nr, nc = r + directions[nd][0], c + directions[nd][1]
            if 0 <= nr < M and 0 <= nc < N and not visit[nr][nc]:
                is_break = False
                break
        if is_break:
            break

        d = (d + 1) % 4
        r, c, cnt = r + directions[d][0], c + directions[d][1], cnt + 1
print(cnt)
