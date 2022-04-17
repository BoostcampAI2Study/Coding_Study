import collections, sys, itertools

def rotate(board, rotate_cnt=1, clockwise=True):
    for _ in range(rotate_cnt): # (-)90, (-)180, (-)270
        board = list(reversed(board)) if clockwise else list(map(list, map(reversed, board))) # list(reversed(temp)) == temp[::-1]
        board = list(map(list, zip(*board)))
    return board

CUBES = []
for _ in range(5):
    layer = [sys.stdin.readline().rstrip().split() for _ in range(5)]
    rotated_layers = [layer] # 0
    for _ in range(3): # 90, 180, 270
        layer = rotate(layer)
        rotated_layers.append(layer)
    CUBES.append(rotated_layers)

min_move_cnts = sys.maxsize
for rotations in itertools.product(range(4), repeat=5):
    # rotating
    rotated_cube = [CUBES[idx][rotate_cnt] for idx, rotate_cnt in enumerate(rotations)]
    
    # stacking
    for new_cube in itertools.permutations(rotated_cube):
        move_cnts = [[[-1]*5 for _ in range(5)] for _ in range(5)]

        if new_cube[0][0][0] == '0' or new_cube[-1][-1][-1] == '0': continue

        Q = collections.deque([(0, 0, 0)]) # height, y, x
        move_cnts[0][0][0] = 0
        while Q:
            height, y, x = Q.popleft()

            if (height, y, x) == (4, 4, 4):
                min_move_cnts = min(min_move_cnts, move_cnts[-1][-1][-1])
                if min_move_cnts == 12: # minimum moves
                    print(12)
                    sys.exit()
                break
            
            if move_cnts[height][y][x] >= min_move_cnts: continue # backtracking

            for new_height, new_y, new_x in (height+1, y, x), (height-1, y, x), (height, y+1, x), (height, y-1, x), (height, y, x+1), (height, y, x-1):
                if 0 <= new_height < 5 and 0 <= new_y < 5 and 0 <= new_x < 5 and new_cube[new_height][new_y][new_x] == '1':
                    if move_cnts[new_height][new_y][new_x] == -1:
                        Q.append((new_height, new_y, new_x))
                        move_cnts[new_height][new_y][new_x] = move_cnts[height][y][x]+1

print(min_move_cnts if min_move_cnts != sys.maxsize else -1)