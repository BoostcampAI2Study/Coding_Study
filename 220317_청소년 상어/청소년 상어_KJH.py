
from collections import defaultdict
from copy import deepcopy


DIRECTION_MAP = {
    0: (-1, 0),
    1: (-1, -1),
    2: (0, -1),
    3: (1, -1),
    4: (1, 0),
    5: (1, 1),
    6: (0, 1),
    7: (-1, 1),
}

BOARD = [[0] * 4 for _ in range(4)]
FISH_INFO = defaultdict(list)  # position, direction

for i in range(4):
    line = list(map(int, input().split()))
    for j in range(0, len(line), 2):
        col = j // 2
        BOARD[i][col] = line[j]
        FISH_INFO[line[j]].append((i, col))
        FISH_INFO[line[j]].append(line[j + 1] - 1)

SHARK_INFO = [(0, 0), FISH_INFO[BOARD[0][0]][1]]
first_fish = BOARD[0][0]
FISH_INFO.pop(BOARD[0][0])
BOARD[0][0] = 0
answer = 0


def fish_update(FISH_INFO: dict, BOARD, SHARK_INFO):
    for fish in sorted(FISH_INFO.keys()):
        if FISH_INFO[fish]:
            (r, c), dir = FISH_INFO[fish]
            for direction in range(dir, dir + 8):
                direction = direction % 8
                dr, dc = DIRECTION_MAP[direction]
                nr, nc = r + dr, c + dc
                if 0 <= nr < 4 and 0 <= nc < 4:
                    if (nr, nc) != SHARK_INFO[0]:
                        FISH_INFO[fish] = [(nr, nc), direction]
                        if BOARD[nr][nc]:
                            FISH_INFO[BOARD[nr][nc]][0] = (r, c)
                        BOARD[r][c], BOARD[nr][nc] = BOARD[nr][nc], BOARD[r][c]
                        break
    return FISH_INFO, BOARD


def move_shark(SHARK_INFO, FISH_INFO, BOARD, ate_fishes):
    global answer
    (r, c), dir = SHARK_INFO
    dr, dc = DIRECTION_MAP[dir]
    nr, nc = r + dr, c + dc
    FISH_INFO, BOARD = fish_update(FISH_INFO, BOARD, SHARK_INFO)
    shark_eat = False
    while 0 <= nr < 4 and 0 <= nc < 4:
        if BOARD[nr][nc]:
            shark_eat = True
            fish, (pos, fish_dir) = BOARD[nr][nc], FISH_INFO[BOARD[nr][nc]]
            FISH_INFO.pop(fish)
            BOARD[nr][nc] = 0
            move_shark(
                [(nr, nc), fish_dir],
                deepcopy(FISH_INFO),
                deepcopy(BOARD),
                ate_fishes + fish,
            )
            FISH_INFO[fish] = [pos, fish_dir]
            BOARD[nr][nc] = fish
        nr += dr
        nc += dc
    if not shark_eat:
        answer = max(answer, ate_fishes)


move_shark(SHARK_INFO, FISH_INFO, BOARD, first_fish)
print(answer)
