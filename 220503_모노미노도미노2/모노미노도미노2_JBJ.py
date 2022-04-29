BLUE_BOARD, GREEN_BOARD = [[False]*6 for _ in range(4)], [[False]*4 for _ in range(6)]
N = int(input().rstrip())
score = 0

for _ in range(N):
    T, Y, X = map(int, input().rstrip().split())

    if T == 1: # 1x1 block
        blue_block, green_block = [(Y, 0)], [(0, X)]
    elif T == 2: # 1x2 block
        blue_block, green_block = [(Y, 0), (Y, 1)], [(0, X), (0, X+1)]
    else: # 2x1 block
        blue_block, green_block = [(Y, 0), (Y+1, 0)], [(0, X), (1, X)]

    # BLUE_BOARD: column-wise
    # position the new blue block.
    while True:
        new_blue_block, move_flag = [(y, x+1) for y, x in blue_block], True
        for y, x in new_blue_block:
            if x > 5 or BLUE_BOARD[y][x]: move_flag = False
        if move_flag:
            blue_block = new_blue_block
        else:
            break
    for y, x in blue_block: BLUE_BOARD[y][x] = True
    
    # full column check.
    for x in range(2, 6):
        if BLUE_BOARD[0][x] and BLUE_BOARD[1][x] and BLUE_BOARD[2][x] and BLUE_BOARD[3][x]:
            score += 1
            for nx in range(x, 0, -1): # move the column towards.
                BLUE_BOARD[0][nx], BLUE_BOARD[1][nx], BLUE_BOARD[2][nx], BLUE_BOARD[3][nx] = BLUE_BOARD[0][nx-1], BLUE_BOARD[1][nx-1], BLUE_BOARD[2][nx-1], BLUE_BOARD[3][nx-1]
            BLUE_BOARD[0][0], BLUE_BOARD[1][0], BLUE_BOARD[2][0], BLUE_BOARD[3][0] = False, False, False, False
    
    # light blue zone operation.
    col_0_flag, col_1_flag = False, False
    if BLUE_BOARD[0][0] or BLUE_BOARD[1][0] or BLUE_BOARD[2][0] or BLUE_BOARD[3][0]: col_0_flag = True
    if BLUE_BOARD[0][1] or BLUE_BOARD[1][1] or BLUE_BOARD[2][1] or BLUE_BOARD[3][1]: col_1_flag = True

    move_cnt = 2 if col_0_flag else (1 if col_1_flag else 0)
    if move_cnt:
        for x in range(5, move_cnt-1, -1):
            BLUE_BOARD[0][x], BLUE_BOARD[1][x], BLUE_BOARD[2][x], BLUE_BOARD[3][x] = BLUE_BOARD[0][x-move_cnt], BLUE_BOARD[1][x-move_cnt], BLUE_BOARD[2][x-move_cnt], BLUE_BOARD[3][x-move_cnt]
        for x in range(move_cnt):
            BLUE_BOARD[0][x], BLUE_BOARD[1][x], BLUE_BOARD[2][x], BLUE_BOARD[3][x] = False, False, False, False

    # GREEN_BOARD: row-wise
    # position the new green block.
    while True:
        new_green_block, move_flag = [(y+1, x) for y, x in green_block], True
        for y, x in new_green_block:
            if y > 5 or GREEN_BOARD[y][x]: move_flag = False
        if move_flag:
            green_block = new_green_block
        else:
            break
    for y, x in green_block: GREEN_BOARD[y][x] = True
    
    # full row check.
    for y in range(2, 6):
        if GREEN_BOARD[y][0] and GREEN_BOARD[y][1] and GREEN_BOARD[y][2] and GREEN_BOARD[y][3]:
            score += 1
            for ny in range(y, 0, -1): # move the row towards.
                GREEN_BOARD[ny][0], GREEN_BOARD[ny][1], GREEN_BOARD[ny][2], GREEN_BOARD[ny][3] = GREEN_BOARD[ny-1][0], GREEN_BOARD[ny-1][1], GREEN_BOARD[ny-1][2], GREEN_BOARD[ny-1][3]
            GREEN_BOARD[0][0], GREEN_BOARD[0][1], GREEN_BOARD[0][2], GREEN_BOARD[0][3] = False, False, False, False
    
    # light green zone operation.
    row_0_flag, row_1_flag = False, False
    if GREEN_BOARD[0][0] or GREEN_BOARD[0][1] or GREEN_BOARD[0][2] or GREEN_BOARD[0][3]: row_0_flag = True
    if GREEN_BOARD[1][0] or GREEN_BOARD[1][1] or GREEN_BOARD[1][2] or GREEN_BOARD[1][3]: row_1_flag = True

    move_cnt = 2 if row_0_flag else (1 if row_1_flag else 0)
    if move_cnt:
        for y in range(5, move_cnt-1, -1):
            GREEN_BOARD[y][0], GREEN_BOARD[y][1], GREEN_BOARD[y][2], GREEN_BOARD[y][3] = GREEN_BOARD[y-move_cnt][0], GREEN_BOARD[y-move_cnt][1], GREEN_BOARD[y-move_cnt][2], GREEN_BOARD[y-move_cnt][3]
        for y in range(move_cnt):
            GREEN_BOARD[y][0], GREEN_BOARD[y][1], GREEN_BOARD[y][2], GREEN_BOARD[y][3] = False, False, False, False

print(score)
print(sum(map(sum, BLUE_BOARD)) + sum(map(sum, GREEN_BOARD)))