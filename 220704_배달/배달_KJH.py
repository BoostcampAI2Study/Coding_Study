from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
FIND = False
goals = []
for r in range(N):
    for c in range(M):
        if board[r][c] == "S":
            minsik = (r, c)
        elif board[r][c] == "C":
            goals.append((r, c))


dir_map = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(s_r, s_c, dir=-1):
    global board
    visited = [[[[0] * 3 for _ in range(4)] for _ in range(M)] for _ in range(N)]
    q = deque([(s_r, s_c, 0, dir, 0)])

    while q:
        r, c, dist, direct, find_goal = q.popleft()
        if board[r][c] == "C":
            for i in range(2):
                if (r, c) == goals[i] and find_goal != i + 1:
                    find_goal += i + 1
            if find_goal == 3:
                return dist

        for n_dir in range(4):
            dr, dc = dir_map[n_dir]
            nr, nc = r + dr, c + dc
            if direct == n_dir:
                continue
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != "#":
                if not visited[nr][nc][n_dir][find_goal]:
                    visited[nr][nc][n_dir][find_goal] = 1
                    q.append((nr, nc, dist + 1, n_dir, find_goal))
    return -1


print(bfs(minsik[0], minsik[1]))
