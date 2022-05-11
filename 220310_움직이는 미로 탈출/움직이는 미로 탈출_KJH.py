# https://www.acmicpc.net/problem/16954

from collections import deque
import sys

input = sys.stdin.readline

board = deque([input().strip() for _ in range(8)])


def update_board():
    board.pop()
    board.appendleft("." * 8)


q = deque(
    [
        (7 + dr, 0 + dc, 1)
        for dr, dc in [
            (0, 0),
            (1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 0),
            (-1, 1),
            (-1, -1),
        ]
        if 0 <= 7 + dr < 8 and 0 <= dc < 8 and board[7 + dr][dc] != "#"
    ]
)
prev_time = 0
visited = set()
while q:
    r, c, time = q.popleft()
    if prev_time != time:
        update_board()
        prev_time = time
    if board[r][c] == "#":
        continue
    if (r, c) == (0, 7):
        print(1)
        sys.exit()
    for dr, dc in [
        (0, 0),
        (1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 0),
        (-1, 1),
        (-1, -1),
    ]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 8 and 0 <= nc < 8 and (nr, nc, time + 1) not in visited:
            if board[nr][nc] != "#":
                visited.add((nr, nc, time + 1))
                q.append((nr, nc, time + 1))
print(0)
