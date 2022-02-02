# input func
def input_func(N):
    global puzzle, is_dominoes
    dict_row = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8}
    input_domino = [input().split() for _ in range(N)]
    input_loc = input().split()

    for domino in input_domino:
        num1, loc1, num2, loc2 = domino
        num1, num2 = int(num1), int(num2)
        loc1_r, loc1_c = dict_row[loc1[0]], int(loc1[1]) - 1
        loc2_r, loc2_c = dict_row[loc2[0]], int(loc2[1]) - 1
        puzzle[loc1_r][loc1_c] = num1
        puzzle[loc2_r][loc2_c] = num2
        is_dominoes[num1][num2] = True

    for i, loc in enumerate(input_loc):
        r, c = dict_row[loc[0]], int(loc[1]) - 1
        puzzle[r][c] = i + 1

# check row
def check_row(check_r, check_num):
    global puzzle
    for c in range(9):
        if puzzle[check_r][c] == check_num:
            return False
    return True

# check column
def check_col(check_c, check_num):
    global puzzle
    for r in range(9):
        if puzzle[r][check_c] == check_num:
            return False
    return True

# check grid
def check_box(check_r, check_c, check_num):
    global puzzle
    check_r, check_c = check_r // 3, check_c // 3
    for r in range(3 * check_r, 3 * check_r + 3):
        for c in range(3 * check_c, 3 * check_c + 3):
            if puzzle[r][c] == check_num:
                return False
    return True

# Comprehensively check
def check_puzzle(check_r, check_c, check_num):
    return check_row(check_r, check_num) and check_col(check_c, check_num) and check_box(check_r, check_c, check_num)

def dfs(loc):
    global puzzle, is_dominoes, cnt
    # right, down
    NR = [0, 1]
    NC = [1, 0]
    # output
    if loc == 80:
        if puzzle[8][8] == 0:
            return False
        print("Puzzle", cnt)
        cnt += 1
        for row in range(9):
            print(''.join(map(str, puzzle[row])))
        # escape if find answer using [return True]
        return True

    r, c = loc // 9, loc % 9
    for idx in range(2):
        nr, nc = r + NR[idx], c + NC[idx]
        # Exceptions
        if nr < 0 or nr > 8 or nc < 0 or nc > 8:
            continue
        if puzzle[nr][nc] != 0 and puzzle[r][c] == 0:
            continue
        # pruning 
        if puzzle[r][c] != 0:
            if dfs(loc + 1):
                return True
            return False
        # Complete exploration
        for domino_i in range(1, 10):
            for domino_j in range(domino_i + 1, 10):
                if is_dominoes[domino_i][domino_j] or is_dominoes[domino_j][domino_i]:
                    continue
                if check_puzzle(r, c, domino_i) and check_puzzle(nr, nc, domino_j):
                    puzzle[r][c] = domino_i
                    puzzle[nr][nc] = domino_j
                    is_dominoes[domino_i][domino_j] = True
                    # pruning   
                    if dfs(loc + 1):
                        return True
                    puzzle[r][c] = 0
                    puzzle[nr][nc] = 0
                    is_dominoes[domino_i][domino_j] = False

                if check_puzzle(r, c, domino_j) and check_puzzle(nr, nc, domino_i):
                    puzzle[r][c] = domino_j
                    puzzle[nr][nc] = domino_i
                    is_dominoes[domino_j][domino_i] = True
                    # pruning   
                    if dfs(loc + 1):
                        return True
                    puzzle[r][c] = 0
                    puzzle[nr][nc] = 0
                    is_dominoes[domino_j][domino_i] = False
    return False

cnt = 1
while True:
    N = int(input())
    if N == 0:
        break

    puzzle = [[0] * 9 for _ in range(9)]
    is_dominoes = [[False] * 10 for _ in range(10)]

    input_func(N)
    dfs(0)
    
# Language : PyPy3
# Memory : 145632 kb
# Time : 924 ms
# 혜원님 코드 기반으로 수정