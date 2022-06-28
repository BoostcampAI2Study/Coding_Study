# https://www.acmicpc.net/problem/16973

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
H, W, S_r, S_c, F_r, F_c = map(int, input().split())
S_r, S_c, F_r, F_c = S_r - 1, S_c - 1, F_r - 1, F_c - 1
block = []
for r in range(N):
    for c in range(M):
        if board[r][c]:
            block.append((r, c))


def check_block(r, c):
    for br, bc in block:
        if r <= br < r + H and c <= bc < c + W:
            return False
    return True


def bfs(sr, sc):
    q = deque([(sr, sc, 0)])
    visited = [[0] * M for _ in range(N)]
    visited[sr][sc] = 1
    while q:
        r, c, cnt = q.popleft()
        if (r, c) == (F_r, F_c):
            return cnt
        for dr, dc in [(0, 1), (-1, 0), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < N
                and 0 <= nc < M
                and 0 <= nr + H - 1 < N
                and 0 <= nc + W - 1 < M
            ):
                if not visited[nr][nc] and check_block(nr, nc):
                    visited[nr][nc] = 1
                    q.append((nr, nc, cnt + 1))
    return -1


print(bfs(S_r, S_c))
