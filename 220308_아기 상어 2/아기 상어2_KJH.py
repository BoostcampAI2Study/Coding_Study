from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
SHARK_POS = []
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j]:
            SHARK_POS.append((i, j))
    board.append(line)


def bfs(shark_pos):
    global M, N
    visited = [[-1] * M for _ in range(N)]
    max_dis = 0
    q = deque([((x, y), 0) for x, y in shark_pos])
    while q:
        (x, y), time = q.popleft()
        if visited[x][y] != -1:
            max_dis = max(max_dis, time - 1, visited[x][y])
            continue
        visited[x][y] = time

        for dx, dy in [
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
            (1, 0),
            (-1, 0),
        ]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == -1:
                    q.append(((nx, ny), time + 1))
    return max_dis


print(bfs(SHARK_POS))
