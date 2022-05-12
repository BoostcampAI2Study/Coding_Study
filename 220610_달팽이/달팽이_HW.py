import sys
N = int(sys.stdin.readline())
LOC_N = int(sys.stdin.readline())

board = [[0] * N for _ in range(N)]
moves = []
for i in range(1, N):
    moves += [i] * 2
moves.append(N - 1)

directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)} # 상우하좌
board[N // 2][N // 2] = 1
cnt = 1
cur_r, cur_c, cur_d = N // 2, N // 2, 0
for move in moves:
    for i in range(move):
        cnt += 1
        cur_r, cur_c = cur_r + directions[cur_d][0], cur_c + directions[cur_d][1]
        board[cur_r][cur_c] = cnt
    cur_d = (cur_d + 1) % 4

locations = []
for r in range(N):
    print(' '.join(map(str, board[r])))
    for c in range(N):
        if board[r][c] == LOC_N:
            locations = [r + 1, c + 1]
print(' '.join(map(str, locations)))
