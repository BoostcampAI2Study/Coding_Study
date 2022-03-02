import copy, sys
sys.setrecursionlimit(10 ** 6)

direction = {0: (-1, 0), 1: (-1, -1), 2: (0, -1), 3: (1, -1), 4: (1, 0), 5: (1, 1), 6: (0, 1), 7: (-1, 1)}
board = []
for r in range(4):
    board.append([])
    fishes = list(map(int, sys.stdin.readline().strip().split()))
    for c in range(4):
        board[r].append([fishes[2 * c], fishes[2 * c + 1]])  # size, direction

catch_size = 0
# dfs
def dfs(shark_r, shark_c, size, new_board):
    global catch_size
    catch_size = max(catch_size, size)
    # move fishes
    for i in range(1, 17):
        fish_d = -1
        for r in range(4):
            for c in range(4):
                if new_board[r][c][0] == i:
                    fish_r, fish_c, fish_d = r, c, new_board[r][c][1] - 1
        if fish_d != -1:
            for d in range(8):
                nd = (fish_d + d) % 8
                nr, nc = direction[nd][0] + fish_r, direction[nd][1] + fish_c
                # out of bound or meet shark: change the direction
                if 0 <= nr < 4 and 0 <= nc < 4:
                    if nr == shark_r and nc == shark_c:
                        continue
                    # meet fish or blank space: swap
                    swap_num = new_board[fish_r][fish_c][0]
                    new_board[fish_r][fish_c] = new_board[nr][nc][:]
                    new_board[nr][nc][0], new_board[nr][nc][1] = swap_num, nd + 1
                    break
    # shark
    shark_d = new_board[shark_r][shark_c][1]
    for i in range(1, 4):
        nr, nc = shark_r + i * direction[shark_d - 1][0], shark_c + i * direction[shark_d - 1][1]
        if 0 <= nr < 4 and 0 <= nc < 4 and new_board[nr][nc][0]:
            fish_size = new_board[nr][nc][0]
            new_board[nr][nc][0] = 0
            dfs(nr, nc, size + fish_size, copy.deepcopy(new_board))
            new_board[nr][nc][0] = fish_size
# shark = (0, 0)
size = board[0][0][0]
board[0][0][0] = 0
dfs(0, 0, size, board)
print(catch_size)
