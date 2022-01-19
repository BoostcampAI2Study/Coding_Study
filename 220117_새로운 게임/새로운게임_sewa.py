import sys

def UpdateLocation(horse_info, horses, togo_r, togo_c):
    for horse in horses:
        horse_info[horse][0], horse_info[horse][1] = togo_r, togo_c
    return horse_info

def OutOfBoard(N, togo_r, togo_c):
    if togo_r < 0 or togo_r > N-1:
        return True
    if togo_c < 0 or togo_c > N-1:
        return True
    return False

def ReverseDirection(horse_info, horse):
    if horse_info[horse][2] == 1:
        horse_info[horse][2] = 2
    elif horse_info[horse][2] == 2:
        horse_info[horse][2] = 1
    elif horse_info[horse][2] == 3:
        horse_info[horse][2] = 4
    elif horse_info[horse][2] == 4:
        horse_info[horse][2] = 3
    return horse_info, horse_info[horse][2]

def ToGo(N, horse_r, horse_c, horse_dir):
    direction = {1:[0,1], 2:[0,-1], 3:[-1, 0], 4:[1,0]}
    togo_r = horse_r + direction[horse_dir][0]
    togo_c = horse_c + direction[horse_dir][1]
    if OutOfBoard(N, togo_r, togo_c):
        return -1, -1
    return togo_r, togo_c
    
def MaxBuild(board):
    last_max = 0
    for r in board:
        for horses in r:
            if len(horses) > last_max:
                last_max = len(horses)
    if last_max >= 4:
        return True
    return False

def Move(N, horse_info, horse, board_info, board, flag):
    horse_r, horse_c, horse_dir = horse_info[horse]    
    togo_r, togo_c = ToGo(N, horse_r, horse_c, horse_dir)
    if board_info[togo_r][togo_c] == 2 or (togo_r,togo_c) == (-1,-1):
        horse_info, horse_dir = ReverseDirection(horse_info, horse)
        if not flag:
            return Move(N, horse_info, horse, board_info, board, True) 
    elif board_info[togo_r][togo_c] == 0:
        board[togo_r][togo_c].extend(board[horse_r][horse_c])
        horse_info = UpdateLocation(horse_info, board[horse_r][horse_c], togo_r, togo_c)
        board[horse_r][horse_c] = []
    elif board_info[togo_r][togo_c] == 1:
        board[togo_r][togo_c].extend(reversed(board[horse_r][horse_c]))
        horse_info = UpdateLocation(horse_info, board[horse_r][horse_c], togo_r, togo_c)
        board[horse_r][horse_c] = []
    return horse_info, board_info, board

def Chess(N,K,board_info, horse_info, board):
    for count in range(1, 1001):
        for horse in range(1, K+1):
            horse_r, horse_c, horse_dir = horse_info[horse]
            if board[horse_r][horse_c][0] != horse :
                continue
            
            horse_info, board_info, board = Move(N, horse_info, horse, board_info, board, False)
            
        if MaxBuild(board):
            return count

    return -1



N, K = map(int, sys.stdin.readline().split())
board_info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
horse_info = {}
board = [[[] for _ in range(N)] for _ in range(N)]

for horse in range(1, K+1):
    r,c,dir = map(int, sys.stdin.readline().split())
    board[r-1][c-1].append(horse)
    horse_info[horse] = [r-1,c-1,dir] 


print(Chess(N,K,board_info, horse_info, board))