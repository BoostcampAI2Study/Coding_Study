import sys
N, M = map(int, sys.stdin.readline().split())
BOARD = [sys.stdin.readline() for _ in range(N)]

visit = [[False] * M for _ in range(N)]
results = []

for r in range(1, N - 1):
    for c in range(1, M - 1):
        if BOARD[r][c] == '*':
            directions = [0] * 4    # up, down, right, left
            for idx, (dr, dc) in enumerate([(-1, 0), (1, 0), (0, 1), (0, -1)]):
                nr, nc = r + dr, c + dc
                while True:
                    if nr < 0 or nr >= N or nc < 0 or nc >= M or BOARD[nr][nc] == '.':
                        break
                    nr, nc = nr + dr, nc + dc
                    directions[idx] += 1
            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                for _ in range(min(directions)):
                    visit[nr][nc] = True
                    nr, nc = nr + dr, nc + dc

            for i in range(1, min(directions) + 1):
                visit[r][c] = True
                results.append(str(r + 1) + ' ' + str(c + 1) + ' ' + str(i))

is_cross = True
for r in range(N):
    for c in range(M):
        if BOARD[r][c] == '*' and visit[r][c] == False:
            is_cross = False
            break

if is_cross:
    print(len(results))
    for result in results:
        print(result)
else:
    print(-1)
