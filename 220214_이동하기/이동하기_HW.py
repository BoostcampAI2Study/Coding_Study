N, M = map(int, input().split())
candy_board = [list(map(int, input().split())) for _ in range(N)]
board = [[0] * M for _ in range(N)]
NR = [1, 0, 1]
NC = [0, 1, 1]

board[0][0] = candy_board[0][0]
for r in range(N):
    for c in range(M):
        for i in range(3):
            nr, nc = r + NR[i], c + NC[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            board[nr][nc] = max(board[nr][nc], board[r][c] + candy_board[nr][nc])

print(board[N - 1][M - 1])