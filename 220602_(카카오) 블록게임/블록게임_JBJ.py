def solution(board):
    
    def is_black_block(y, x):
        nonlocal board
        for cy in range(0, y+1):
            if board[cy][x]: return False
        return True
    
    def rectangle_check(y, x, dy, dx):
        nonlocal board
        color_block_idx, black_block_cnt = -1, 0
        for cy in range(y, y+dy): # rectangle fit check (2x3 or 3x2).
            for cx in range(x, x+dx):
                if board[cy][cx]: # block space
                    if color_block_idx == -1:
                        color_block_idx = board[cy][cx]
                    elif color_block_idx != board[cy][cx]:
                        return False
                else: # empty space
                    if not is_black_block(cy, cx): return False
                    black_block_cnt += 1
                    if black_block_cnt > 2: return False
        
        for cy in range(y, y+dy): # eliminate the block.
            for cx in range(x, x+dx):
                board[cy][cx] = 0
        return True
    
    N = len(board)
    total_elimination_cnt = 0
    while True:
        elimination_cnt = 0
        for y in range(N):
            for x in range(N):
                if y <= N-2 and x <= N-3 and rectangle_check(y, x, 2, 3): # 2x3
                    elimination_cnt += 1
                if y <= N-3 and x <= N-2 and rectangle_check(y, x, 3, 2): # 3x2
                    elimination_cnt += 1

        if elimination_cnt:
            total_elimination_cnt += elimination_cnt
        else:
            return total_elimination_cnt
