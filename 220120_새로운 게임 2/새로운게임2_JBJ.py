import sys

def solution():
    DY = (0, 0, -1, 1)
    DX = (1, -1, 0, 0)
    CHANGE_DIRECTION = {0:1, 1:0, 2:3, 3:2}

    N, K = map(int, sys.stdin.readline().strip().split())
    BOARD = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    horses_info = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(K)]
    horses_info = [[y-1, x-1, direction-1] for y, x, direction in horses_info]

    horses = [[[] for _ in range(N)] for _ in range(N)]
    for idx, (y, x, _) in enumerate(horses_info):
        horses[y][x].append(idx)
    turn = 0

    while turn <= 1000: # until 1000 turns
        turn += 1
        for horse_num in range(K): # move horses in order of horse numbers
            cur_y, cur_x, direction = horses_info[horse_num]
            idx = horses[cur_y][cur_x].index(horse_num) # update horse_num ~ upper horses
            new_y, new_x = cur_y + DY[direction], cur_x + DX[direction]

            # out of board or blue board check
            if not 0 <= new_y < N or not 0 <= new_x < N or BOARD[new_y][new_x] == 2:
                direction = CHANGE_DIRECTION[direction]
                new_y, new_x = cur_y + DY[direction], cur_x + DX[direction]
                horses_info[horse_num][2] = direction 
                # out of board or blue board check again
                if not 0 <= new_y < N or not 0 <= new_x < N or BOARD[new_y][new_x] == 2:
                    continue
                
            # horses info update
            for horse in horses[cur_y][cur_x][idx:]:
                horses_info[horse][0], horses_info[horse][1] = new_y, new_x

            # move horses to new location
            if BOARD[new_y][new_x] == 0: # white board
                horses[new_y][new_x].extend(horses[cur_y][cur_x][idx:])
                del horses[cur_y][cur_x][idx:]
            if BOARD[new_y][new_x] == 1: #red board
                horses[new_y][new_x].extend(horses[cur_y][cur_x][idx:][::-1])
                del horses[cur_y][cur_x][idx:]
            
            # check the number of horses
            if len(horses[new_y][new_x]) >= 4:
                return turn

    return -1

print(solution())