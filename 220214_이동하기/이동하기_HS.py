from collections import deque
import copy

def _input():
    return list(map(int, input().split()))

N, M = _input()
maze = [_input() for _ in range(N)]
new_maze = [[0]*M for _ in range(N)]
new_maze[0][0] = maze[0][0]

move = [(1, 0), (0, 1)]

q = deque([(0, 0)])
while q:
    y, x = q.popleft()
    for my, mx in move:
        ny, nx = y + my, x + mx
        if 0 <= ny < N and 0 <= nx < M:
            if new_maze[ny][nx] < new_maze[y][x] + maze[ny][nx]:
                new_maze[ny][nx] = new_maze[y][x] + maze[ny][nx]
                q.append((ny, nx))

print(new_maze[N-1][M-1])
