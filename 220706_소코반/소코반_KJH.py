# https://www.acmicpc.net/problem/4577

import sys

input = sys.stdin.readline

dir_map = {"U": (-1, 0), "L": (0, -1), "D": (1, 0), "R": (0, 1)}


def move(r, c, dir):
    global board, goals_num
    past_pos = "." if board[r][c] == "w" else "+"
    nr, nc = r + dir_map[dir][0], c + dir_map[dir][1]

    if board[nr][nc] == "#":
        pass
    elif board[nr][nc] == ".":
        board[nr][nc], board[r][c] = "w", past_pos

    elif board[nr][nc] == "b":
        tmp_r, tmp_c = nr + dir_map[dir][0], nc + dir_map[dir][1]
        if board[tmp_r][tmp_c] in ".":
            board[nr][nc], board[r][c], board[tmp_r][tmp_c] = "w", past_pos, "b"
        elif board[tmp_r][tmp_c] in "+":
            board[nr][nc], board[r][c], board[tmp_r][tmp_c] = "w", past_pos, "B"
            goals_num -= 1
    elif board[nr][nc] == "+":
        board[nr][nc], board[r][c] = "W", past_pos
    elif board[nr][nc] == "B":
        tmp_r, tmp_c = nr + dir_map[dir][0], nc + dir_map[dir][1]
        if board[tmp_r][tmp_c] in ".":
            board[nr][nc], board[r][c], board[tmp_r][tmp_c] = "W", past_pos, "b"
            goals_num += 1
        elif board[tmp_r][tmp_c] in "+":
            board[nr][nc], board[r][c], board[tmp_r][tmp_c] = "W", past_pos, "B"
    return (nr, nc) if board[nr][nc] in "wW" else (r, c)


game_cnt = 0
while 1:
    game_cnt += 1
    R, C = map(int, input().split())
    if (R, C) == (0, 0):
        break
    board = [list(input().strip()) for _ in range(R)]
    command = input().strip()
    pos_r, pos_c = None, None
    goals_num = 0
    for r in range(R):
        for c in range(C):
            if board[r][c] == "w":
                pos_r, pos_c = r, c
            elif board[r][c] == "W":
                pos_r, pos_c = r, c
                goals_num += 1
            elif board[r][c] == "+":
                goals_num += 1
    for com in command:
        pos_r, pos_c = move(pos_r, pos_c, com)
        if not goals_num:
            break
    result = "incomplete" if goals_num != 0 else "complete"
    print(f"Game {game_cnt}: {result}")
    for line in board:
        print("".join(line))
