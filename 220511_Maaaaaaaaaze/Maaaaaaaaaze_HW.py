import sys, collections, itertools
def bfs():
    q = collections.deque()
    q.append((0, 0, 0, 0))
    visit = [[[False] * 5 for _ in range(5)] for _ in range(5)]
    visit[0][0][0] = True

    while q:
        r, c, h, move = q.popleft()
        if r == 4 and c == 4 and h == 4:
            return move

        for nr, nc, nh in [(0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]:
            nr, nc, nh = nr + r, nc + c, nh + h
            if 0 <= nr < 5 and 0 <= nc < 5 and 0 <= nh < 5 and not visit[nh][nr][nc] and update_map[nh][nr][nc]:
                q.append((nr, nc, nh, move + 1))
                visit[nh][nr][nc] = True
    return 1e9

def rotate(h):
    global update_map
    new_board = [[0] * 5 for _ in range(5)]

    for r in range(5):
        for c in range(5):
            new_board[c][4 - r] = update_map[h][r][c]

    for r in range(5):
        for c in range(5):
            update_map[h][r][c] = new_board[r][c]

def rotate_all_board():
    global min_result
    for _ in range(4):
        rotate(0)
        if update_map[0][0][0]:
            for _ in range(4):
                rotate(1)
                for _ in range(4):
                    rotate(2)
                    for _ in range(4):
                        rotate(3)
                        for _ in range(4):
                            rotate(4)
                            if update_map[4][4][4]:
                                min_result = min(min_result, bfs())

BOARD = [[list(map(int, sys.stdin.readline().split())) for _ in range(5)] for _ in range(5)]
min_result = 1e9
for candidates in list(itertools.permutations(range(5))):
    update_map = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    for h in range(5):
        update_map[candidates[h]] = BOARD[h]
        rotate_all_board()
print(min_result) if min_result != 1e9 else print(-1)
