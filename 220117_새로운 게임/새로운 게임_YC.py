import sys
input = sys.stdin.readline

def nextblock(row,col,direction):
    if direction == 1:
        if col == N-1: return -1
        else: return color[row][col+1]
    elif direction == 2:
        if col == 0: return -1
        else: return color[row][col-1]
    elif direction == 3:
        if row == 0: return -1
        else: return color[row-1][col]
    elif direction == 4:
        if row == N-1: return -1
        else: return color[row+1][col]

def move(row,col,direction):
    # 1=right, 2=left, 3=up, 4=down
    if direction == 1: return row, col+1
    elif direction == 2: return row, col-1
    elif direction == 3: return row-1, col
    elif direction == 4: return row+1, col

def change_d(direction):
    if direction==1: return 2
    elif direction==2: return 1
    elif direction==3: return 4
    elif direction==4: return 3

def check(horse, row, col, direction, block_color):
    # 0=white, 1=red, 2=blue
    if block_color == 2 or block_color == -1:
        new_row, new_col = row, col
    else:
        new_row, new_col = move(row,col,direction)

        if block_color == 1:
            positions[row][col].reverse()

        while positions[row][col]:
            stack_h = positions[row][col].pop(0)  # 말 칸에서 빼기

            horses[stack_h][0] = [new_row, new_col] # 말 정보 업데이트

            positions[new_row][new_col].append(stack_h)   # 말 새로운 칸에 넣기

        
    
    return new_row, new_col

def solution():
    for cnt in range(1, 1001):
        for horse, info in horses.items():
            (row,col),direction=info

            ## 가장 아래있는 말 아니면 pass
            if positions[row][col][0] != horse:
                continue

            # 0=white, 1=red, 2=blue
            block_color = nextblock(row,col,direction)

            # 파랑이나 끝이면 방향 한 번 바꾸기
            if block_color == 2 or block_color == -1:
                new_direction = change_d(direction)
                horses[horse][1] = new_direction
                
                block_color2 = nextblock(row,col,new_direction)
                new_row, new_col = check(horse, row,col, new_direction, block_color2)        
            else:
                new_row, new_col = check(horse, row,col, direction, block_color)

            if len(positions[new_row][new_col]) >= 4: 
                print(cnt)
                return

    print(-1)
              
N, K = map(int, input().split())

color=[] # 체스판 칸 색
horses={} # 각 말에 대한 정보 ([열,행],방향)
positions=[] # 각 칸에 있는 말 (아래말---윗말)

for _ in range(N):
    color.append(list(map(int, input().split())))
    positions.append([[]*N for _ in range(N)])

for horse in range(1, K+1):
    row, col, direction = map(int, input().split())
    row,col=row-1,col-1

    horses[horse]=[[row,col],direction]
    positions[row][col] = [horse]

solution()