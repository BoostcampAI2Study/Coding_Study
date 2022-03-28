import copy, sys

N = int(sys.stdin.readline().rstrip())
BOARD = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
answer = -1

def left_move(board):
    global N
    for row in range(N):
        numbers, prev_num = [], 0
        for col in range(N):
            if board[row][col]:
                if prev_num and prev_num == board[row][col]: # cur_num == prev_num -> cur_num+prev_num
                    numbers.pop()
                    numbers.append(prev_num*2)
                    prev_num = 0
                else: # prev_num == 0 or prev_num != board[row][col]
                    prev_num = board[row][col]
                    numbers.append(board[row][col])
        
        for col in range(N): # rearrange with numbers -> 0s are padded after assigning numbers
            board[row][col] = numbers[col] if len(numbers) > col else 0

def rotate(board, rotate_cnt, clockwise=True):
    """
    [1, 2, 3]                [7, 8, 9]            [7, 4, 1]
    [4, 5, 6] == reverse ==> [4, 5, 6] == zip ==> [8, 5, 2]   [clockwise]
    [7, 8, 9]                [1, 2, 3]            [9, 6, 3]
    --------------------------------------------------------
    [1, 2, 3]                [3, 2, 1]            [3, 6, 9]
    [4, 5, 6] == reverse ==> [6, 5, 4] == zip ==> [2, 5, 8]   [anti-clockwise]
    [7, 8, 9]                [9, 8, 7]            [1, 4, 7]
    """
    global N
    for _ in range(rotate_cnt): # (-)90, (-)180, (-)270
        board = list(reversed(board)) if clockwise else list(map(list, map(reversed, board))) # list(reversed(temp)) == temp[::-1]
        board = list(map(list, zip(*board)))
    return board

def dfs(move_cnt, board):
    global N, answer
    if move_cnt == 5:
        answer = max(answer, max(map(max, board)))
        return
    
    for rotate_cnt in range(4):
        next_board = copy.deepcopy(board)
        next_board = rotate(next_board, rotate_cnt) # rotate (0, 90, 180, 270 degrees)
        left_move(next_board) # move left
        next_board = rotate(next_board, rotate_cnt, False) # rotate back (0, -90, -180, -270 degrees)
        dfs(move_cnt+1, next_board)

dfs(0, BOARD)
print(answer)