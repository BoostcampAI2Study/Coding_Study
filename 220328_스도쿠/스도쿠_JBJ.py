import collections, sys

SUDOKU = [[0]*10] + [[0]+list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]
POS_ASSIGN_NUMS = collections.defaultdict(set)
EMPTY_SPACES = [(y, x) for y in range(1, 10) for x in range(1, 10) if not SUDOKU[y][x]]

def get_promisings(y, x):
    pos_assign_nums = set(range(1,10))
    global SUDOKU
    # row & col check
    for idx in range(1, 10):
        if SUDOKU[y][idx] in pos_assign_nums: pos_assign_nums.remove(SUDOKU[y][idx])
        if SUDOKU[idx][x] in pos_assign_nums: pos_assign_nums.remove(SUDOKU[idx][x])

    # square check
    sy, sx = (y-1)//3, (x-1)//3
    for y_idx in range((sy*3)+1, (sy*3)+4):
        for x_idx in range((sx*3)+1, (sx*3)+4):
            if SUDOKU[y_idx][x_idx] in pos_assign_nums: pos_assign_nums.remove(SUDOKU[y_idx][x_idx])

    return pos_assign_nums # return promisings

def dfs(empty_space_idx):
    global SUDOKU, EMPTY_SPACES
    if empty_space_idx >= len(EMPTY_SPACES):
        for row in SUDOKU[1:]:
            print(' '.join(map(str,row[1:])))
        sys.exit()
    
    y, x = EMPTY_SPACES[empty_space_idx]
    promisings = get_promisings(y, x)
    for num in promisings:
            SUDOKU[y][x] = num
            dfs(empty_space_idx+1)
            SUDOKU[y][x] = 0
dfs(0)