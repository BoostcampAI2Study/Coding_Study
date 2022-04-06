# https://www.acmicpc.net/problem/14442

from collections import deque
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

table = [list(input().strip()) for _ in range(N)]

visited = [[[0] * M for _ in range(N)] for _ in range(K + 1)]
visited[0][0][0] = 1


def bfs():
    global N, M, K
    q = deque([(0, 0, 0)])  # node, CNT, used_K
    while q:
        x, y, used_K = q.popleft()
        if (x, y) == (N - 1, M - 1):
            return visited[used_K][x][y]

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if table[nx][ny] == "0":
                    if not visited[used_K][nx][ny]:
                        visited[used_K][nx][ny] = visited[used_K][x][y] + 1
                        q.append((nx, ny, used_K))
                elif table[nx][ny] == "1" and used_K < K:
                    if not visited[used_K + 1][nx][ny]:
                        visited[used_K + 1][nx][ny] = visited[used_K][x][y] + 1
                        q.append((nx, ny, used_K + 1))
    return -1


print(bfs())
