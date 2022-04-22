# https://www.acmicpc.net/problem/16236

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
fishs_cnt = [0] * 7
board = []
shark_pos = None
for i in range(N):
    board.append(list(map(int, input().split())))
    for j, fish in enumerate(board[-1]):
        if not fish:
            continue
        elif fish == 9:
            shark_pos = (i, j)
            continue
        fishs_cnt[fish] += 1
board[shark_pos[0]][shark_pos[1]] = 0


def bfs(shark_pos, time):
    global visited, board, shark_size
    q = deque([(shark_pos, time)])  # 상어 위치, 시간
    tmp = []
    while q:
        (x, y), cnt = q.popleft()
        if visited[x][y]:
            continue
        if tmp and tmp[0][-1] < cnt:
            break
        visited[x][y] = 1
        if board[x][y]:
            if board[x][y] < shark_size:
                tmp.append([(x, y), cnt])
                continue
        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and board[nx][ny] <= shark_size:
                    q.append(((nx, ny), cnt + 1))

    return min(tmp, key=lambda x: x[0]) if tmp else (None, time)


shark_size = 2
ate_fishes = 0
time = 0
while sum(fishs_cnt[:shark_size]) != 0:
    visited = [[0] * N for _ in range(N)]
    shark_pos, time = bfs(shark_pos, time)
    if shark_pos == None:
        break
    fishs_cnt[board[shark_pos[0]][shark_pos[1]]] -= 1
    board[shark_pos[0]][shark_pos[1]] = 0
    ate_fishes += 1
    if ate_fishes == shark_size:
        shark_size += 1
        ate_fishes = 0

print(time)
