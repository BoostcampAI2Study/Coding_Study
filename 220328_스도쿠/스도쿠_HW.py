import sys

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]
blank_space = [(r, c) for r in range(9) for c in range(9) if board[r][c] == 0]

def check_row(r, num):
    return False if num in board[r] else True

def check_col(c, num):
    for k in range(9):
        if num == board[k][c]:
            return False
    return True

def check_box(r, c, num):
    check_r, check_c = r // 3 * 3, c // 3 * 3
    for j in range(check_r, check_r + 3):
        for k in range(check_c, check_c + 3):
            if num == board[j][k]:
                return False
    return True

def dfs(idx):
    if idx == len(blank_space) - 1:
        for k in range(9):
            print(' '.join(map(str, board[k])))
        sys.exit()

    for k in range(1,10):
        nr, nc = blank_space[idx + 1]
        if check_row(nr, k) and check_col(nc, k) and check_box(nr, nc, k):
            board[nr][nc] = k
            dfs(idx + 1)
            board[nr][nc] = 0

dfs(-1)
