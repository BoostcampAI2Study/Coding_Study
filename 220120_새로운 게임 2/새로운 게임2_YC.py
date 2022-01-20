import sys
input = sys.stdin.readline

N, K = map(int, input().split())

change_dir = {1:2, 2:1, 3:4, 4:3}

board = []
positions = []
horses={}

def BlockColor(row_col):
    row,col = row_col
    # 0은 흰색, 1은 빨간색, 2는 파란색
    if 0<= row < N and 0<= col < N: return board[row][col]
    else: return -1

def move(row,col,drt):
    # →, ←, ↑, ↓
    if drt==1: return row, col+1
    if drt==2: return row, col-1
    if drt==3: return row-1, col
    if drt==4: return row+1, col

def solution():
    for cnt in range(1000):
        for horse, [[row,col], drt] in horses.items():
            stack = positions[row][col]

            nextblock = BlockColor(move(row,col,drt))

            if nextblock == -1 or nextblock == 2:
                drt = change_dir[drt]
                horses[horse][1] = drt

                nextblock = BlockColor(move(row,col,drt))
                
                if nextblock == -1 or nextblock == 2:
                    continue

            new_row, new_col = move(row,col,drt)

            move_stack = stack[stack.index(horse):]
            if nextblock == 1:
                move_stack.reverse()

            for h in move_stack:
                horses[h][0] = [new_row, new_col]

            positions[new_row][new_col].extend(move_stack)
            positions[row][col] = stack[:stack.index(horse)]

            if len(positions[new_row][new_col]) >= 4:
                print(cnt+1)
                return

    print(-1)

for _ in range(N):
    board.append(list(map(int, input().split())))
    positions.append([[] for _ in range(N)])

for i in range(K):
    row, col, drt = map(int, input().split())
    horses[i+1] = [[row-1,col-1],drt]
    positions[row-1][col-1].extend([i+1])

solution()