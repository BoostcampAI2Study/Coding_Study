import collections, sys
N, M = map(int, sys.stdin.readline().rstrip().split())
BOARD = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
MOVE_DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
OPPOSITE_DIRECTIONS = {0:1, 1:0, 2:3, 3:2}
answer = -1

# get R and B coordinates.
for y in range(N):
    for x in range(M):
        if BOARD[y][x] == 'R':
            BOARD[y][x] = '.'
            R = (y, x)
        elif BOARD[y][x] == 'B':
            BOARD[y][x] = '.'
            B = (y, x)

def move(new_R, new_B, move_direction, is_R_move=True):
    global MOVE_DIRECTIONS
    dy, dx = MOVE_DIRECTIONS[move_direction]
    loc = new_R if is_R_move else new_B
    while True:
            if 0 < loc[0]+dy < N-1 and 0 < loc[1]+dx < M-1 and BOARD[loc[0]+dy][loc[1]+dx] != '#':
                if is_R_move and (loc[0]+dy, loc[1]+dx) == new_B: break # R is blocked by B.
                if not is_R_move and (loc[0]+dy, loc[1]+dx) == new_R: break # B is blocked by R.
                loc = (-1, -1) if BOARD[loc[0]+dy][loc[1]+dx] == 'O' else (loc[0]+dy, loc[1]+dx)
            else:
                break
    return loc

Q = collections.deque([(R, B, 0, -1)]) # [((R_y, R_x), (B_y, B_x), tilt_cnt, prev_move_direction)]
while Q:
    R, B, tilt_cnt, prev_move_direction = Q.popleft()

    for move_direction in range(4):
        if prev_move_direction != -1 and move_direction == OPPOSITE_DIRECTIONS[prev_move_direction]: # backtracking
            continue
        
        new_R, new_B = R, B
        for _ in range(2): # due to blocking by the other ball; move again.
            new_R = move(new_R, new_B, move_direction, True)
            new_B = move(new_R, new_B, move_direction, False)

        if new_B == (-1, -1): # B fell into the hole
            continue
        elif new_R == (-1, -1): # A fell into the hole
            print(tilt_cnt+1)
            sys.exit()
        elif (new_R != R or new_B != B) and tilt_cnt+1 < 10: # tilting succeeded.
            Q.append((new_R, new_B, tilt_cnt+1, move_direction))
print(-1)     