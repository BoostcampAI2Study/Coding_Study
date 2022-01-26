import sys, math

CHAR_2_NUM = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9}
N = int(sys.stdin.readline().strip())
IDX = 1

def sanity_check(y, x, num):
    global puzzle
    # row check
    for x_idx in range(1, 10):
        if puzzle[y][x_idx] == num: 
            return False
    
    # col check
    for y_idx in range(1, 10):
        if puzzle[y_idx][x] == num:
            return False

    # square check
    sy, sx = math.ceil(y/3)-1, math.ceil(x/3)-1
    for y_idx in range((sy*3)+1, (sy*3)+4):
        for x_idx in range((sx*3)+1, (sx*3)+4):
            if puzzle[y_idx][x_idx] == num:
                return False

    return True

def find_first_empty_space():
    global puzzle
    for y in range(1, 10):
        for x in range(1, 10):
            if puzzle[y][x] == 0:
                return y, x
    return -1, -1

def dfs():
    global puzzle, is_domino_used, flag

    y, x = find_first_empty_space()
    
    if y == -1 and x == -1:
        flag = True
        return

    # domino check => right, down
    for next_y, next_x in (y, x+1), (y+1, x):
        if 1 <= next_y <= 9 and 1 <= next_x <= 9 and puzzle[next_y][next_x] == 0:
            for num in range(1, 10):
                for next_num in range(1, 10): # (1 ~ 10): 1036ms, (num+1 ~ 10): 904ms
                    # domino availablility check
                    if num != next_num and not is_domino_used[num][next_num]:
                        # domino fit check (sanity check)
                        if sanity_check(y, x, num) and sanity_check(next_y, next_x, next_num):
                            is_domino_used[num][next_num], is_domino_used[next_num][num] = True, True
                            puzzle[y][x], puzzle[next_y][next_x] = num, next_num
                            
                            dfs()
                            if flag: return
                            
                            puzzle[y][x], puzzle[next_y][next_x] = 0, 0
                            is_domino_used[num][next_num], is_domino_used[next_num][num] = False, False


while N != 0:
    puzzle = [[0] * 10 for _ in range(10)]
    is_domino_used = [[False] * 10 for _ in range(10)]
    flag = False

    for _ in range(N):
        u, lu, v, lv = sys.stdin.readline().strip().split()
        u, y_u, x_u = int(u), CHAR_2_NUM[lu[0]], int(lu[1])
        v, y_v, x_v = int(v), CHAR_2_NUM[lv[0]], int(lv[1])

        puzzle[y_u][x_u] = u
        puzzle[y_v][x_v] = v
        is_domino_used[u][v], is_domino_used[v][u] = True, True
    
    for num, idx in enumerate(sys.stdin.readline().strip().split(), start=1):
        puzzle[CHAR_2_NUM[idx[0]]][int(idx[1])] = num

    dfs()
    print(f'Puzzle {IDX}')
    IDX+=1
    for row in puzzle[1:]:
        print(''.join(map(str, row[1:])))

    N = int(sys.stdin.readline().strip())
