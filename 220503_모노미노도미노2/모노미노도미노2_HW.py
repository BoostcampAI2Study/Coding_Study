import sys

def insert_block(t, r, c, board):
    if t == 4:
        t, c = 2, c - 1

    while True:
        if (t == 1 and r < 9 and not board[r + 1][c]) \
                or (t == 2 and r < 9 and not board[r + 1][c] and not board[r + 1][c + 1]) \
                or (t == 3 and r < 8 and not board[r + 1][c] and not board[r + 2][c]):
            r += 1
            continue
        break

    if t == 1:
        board[r][c] = True
    elif t == 2:
        board[r][c], board[r][c + 1] = True, True
    elif t == 3:
        board[r][c], board[r + 1][c] = True, True
    return board

def remove_row(board):
    global score
    remove_rows = []
    for i in range(6, 10):
        is_remove = True
        for j in range(0, 4):
            if not board[i][j]:
                is_remove = False
                break
        if is_remove:
            remove_rows.append(i)

    for i in remove_rows:
        del board[i]
        board.insert(0, [False] * 4)
        score += 1
    return board

def check_special_row(board):
    special_block = 0
    for check_r in range(5, 3, -1):
        for check_c in range(0, 4):
            if board[check_r][check_c]:
                special_block += 1
                break

    for i in range(special_block):
        del board[9]
        board.insert(0, [False] * 4)
    return board

def count_space(board):
    cnt = 0
    for r in range(6, 10):
        for c in range(0, 4):
            if board[r][c]:
                cnt += 1
    return cnt

N = int(sys.stdin.readline())
BLOCKS = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

blue_board, green_board = [[False] * 4 for _ in range(10)], [[False] * 4 for _ in range(10)]
convert_t = {1: 1, 2: 3, 3: 4}
score = 0

for t, r, c in BLOCKS:
    # insert block in green and blue board
    green_board = insert_block(t, r, c, green_board)
    blue_board = insert_block(convert_t[t], c, 3 - r, blue_board)

    # delete full blocks row
    green_board = remove_row(green_board)
    blue_board = remove_row(blue_board)

    # check special rows
    green_board = check_special_row(green_board)
    blue_board = check_special_row(blue_board)

# count filled spaces
filled_space = 0
filled_space += count_space(blue_board)
filled_space += count_space(green_board)

print(score)
print(filled_space)
