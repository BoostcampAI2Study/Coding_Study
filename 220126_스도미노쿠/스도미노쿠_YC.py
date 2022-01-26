def checkblock(row,col,num,board):
    for r in range(3*(row//3), 3*(row//3)+3):
        for c in range(3*(col//3), 3*(col//3)+3):
            if board[r][c] == num:
                return True
    return False

def checkrow(row, num, board):
    for col in range(9):
        if board[row][col] == num:
            return True
    return False

def checkcol(col, num, board):
    for row in range(9):
        if board[row][col] == num:
            return True
    return False

def checksudomiku(row, col, sudomiku):
    if row < col: sudomiku[row][col] = True
    else: sudomiku[col][row] = True

def asdf(row, col, tmp, sudomiku):
    for t1 in tmp[row][col]:
        for t2 in tmp[row][col+1]:
            if t1 != t2:
                sudomiku[max(t1,t2)][min(t1,t2)].append([row,col])

def solution(board):
    tmp = [[[]for _ in range(9)] for _ in range(9)]
    sudomiku = [[[] for _ in range(10)] for _ in range(10)]

    for num in range(1,10):
        # check row
        for row in range(9):
            if not checkrow(row, num, board):
                # check col
                for col in range(9):
                    # make sure it's board[row][col] is empty before checking
                    if board[row][col]:
                        continue

                    if not checkcol(col, num, board):
                        # check block
                        if not checkblock(row, col, num, board):
                            tmp[row][col].append(num)

    for t in tmp: print(t)
    print("----")

    for row in range(9):
        for col in range(8):
            asdf(row, col, tmp, sudomiku)
    for s in sudomiku: 
        for ss in s:
            print(len(ss), end =" ")
        print("")


d={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8}

import sys
input = sys.stdin.readline

# N = 1
# cnt = 1
# while N != 0:

board = [[[]for _ in range(9)] for _ in range(9)]
sudomiku = [[False for _ in range(i, 9)] for i in range(9)]

N = int(input())
    
for _ in range(N):
    
    U, LU, V, LV = input().split()

    row, col = d[list(LU)[0]], int(list(LU)[1])-1
    board[row][col] = int(U)

    row, col = d[list(LV)[0]], int(list(LV)[1])-1
    board[row][col] = int(V)
 

srt = list(input().split())

for num, s in enumerate(srt):
    row, col = d[list(s)[0]], int(list(s)[1])-1
    board[row][col] = num+1

solution(board)

# for row in range(9):
#     for col in range(8):
#         if not board[row][col] and board[row][col+1]:
#             pass
