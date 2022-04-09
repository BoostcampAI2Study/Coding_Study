def input_func(N):
    global puzzle, dominoes, is_dominoes
    dict_row = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8}
    input_loc = input().split()

    for i in range(N):
        num1, loc1, num2, loc2 = sys.stdin.readline().split()
        num1, loc1_r, loc1_c = int(num1), dict_row[loc1[0]], int(loc1[1]) - 1
        num2, loc2_r, loc2_c = int(num2), dict_row[loc2[0]], int(loc2[1]) - 1

        puzzle[loc1_r][loc1_c], puzzle[loc2_r][loc2_c] = num1, num2
        is_dominoes[num1][num2], is_dominoes[num2][num1] = True, True

    for i, loc in enumerate(input_loc):
        r, c = dict_row[loc[0]], int(loc[1]) - 1
        puzzle[r][c] = i + 1

def check_row(check_r, check_num):
    for c in range(9):
        if puzzle[check_r][c] == check_num:
            return False
    return True

def check_col(check_c, check_num):
    for r in range(9):
        if puzzle[r][check_c] == check_num:
            return False
    return True

def check_box(check_r, check_c, check_num):
    check_r, check_c = check_r // 3, check_c // 3
    for r in range(3 * check_r, 3 * check_r + 3):
        for c in range(3 * check_c, 3 * check_c + 3):
            if puzzle[r][c] == check_num:
                return False
    return True

def check_puzzle(check_r, check_c, check_num):
    return check_row(check_r, check_num) and check_col(check_c, check_num) and check_box(check_r, check_c, check_num)

def dfs(loc):
    global is_finish, cnt
    NR = [0, 1]
    NC = [1, 0]
    
    if is_finish:
        return

    if loc == 81:
        is_finish = True
        print("Puzzle ", cnt)
        for row in range(9):
            print(''.join(map(str, puzzle[row])))
        return

    r, c = loc // 9, loc % 9
    if puzzle[r][c] != 0:
        dfs(loc + 1)
    else:
        for idx in range(2):
            nr, nc = r + NR[idx], c + NC[idx]
            if nr < 0 or nr > 8 or nc < 0 or nc > 8 or puzzle[nr][nc] != 0:
                continue
            for domino_i in range(1, 10):
                for domino_j in range(1, 10):
                    if domino_i == domino_j or is_dominoes[domino_i][domino_j]:
                        continue
                    if check_puzzle(r, c, domino_i) and check_puzzle(nr, nc, domino_j):
                        puzzle[r][c], puzzle[nr][nc] = domino_i, domino_j
                        is_dominoes[domino_i][domino_j], is_dominoes[domino_j][domino_i] = True, True
                        dfs(loc + 1)
                        puzzle[r][c], puzzle[nr][nc] = 0, 0
                        is_dominoes[domino_i][domino_j], is_dominoes[domino_j][domino_i] = False, False

cnt = 1
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    puzzle = [[0] * 9 for _ in range(9)]
    is_dominoes = [[False] * 10 for _ in range(10)]
    is_finish = False

    input_func(N)
    dfs(0)
    cnt += 1
