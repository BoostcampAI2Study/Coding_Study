import copy
import sys
input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

def rotate_1(board, cnt):
    for _ in range(cnt):
        new_board = [[0]*N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                new_board[x][y] = board[y][N-x-1]
        board = new_board
    return board

def rotate_2(board, cnt):
    for _ in range(cnt):
        new_board = [[0]*N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                new_board[x][y] = board[N-y-1][x]
        board = new_board
    return board

def move(board):
    new_board = []
    for x in range(N):
        sub_board = []
        stack = []
        for y in range(N):
            if board[x][y] != 0:
                if not stack:
                    stack.append(board[x][y])
                else:
                    if stack[-1] == board[x][y]:
                        stack[-1] += board[x][y]
                        sub_board += stack
                        stack = []
                    else:
                        stack.append(board[x][y])
        if stack:
            sub_board += stack
        sub_board += [0]*(N-len(sub_board))
        new_board.append(sub_board)

    return new_board

def go_2048(level, board, what):
    global answer
    if level == 5:
        answer = max(answer, max(map(max, board)))
        return
    # 왼쪽
    new_board = move(board)
    go_2048(level+1, new_board, 0)

    copy_board = copy.deepcopy(board)
    for cnt in range(1, 4):
        copy_board_2 = rotate_1(copy_board, cnt)
        copy_board_3 = move(copy_board_2)
        copy_board_2 = rotate_2(copy_board_3, cnt)
        go_2048(level+1, copy_board_2, cnt)


answer = 0
go_2048(0, board, -1)
print(answer)