def _input():
    return list(map(int, input().split()))

N, M = _input()
maze = [_input() for _ in range(N)]
new_maze = [[0]*M for _ in range(N)]
new_maze[0][0] = maze[0][0]

move = [(1, 0), (0, 1)]

for y in range(N):
    for x in range(M):
        for my, mx in move:
            ny, nx = y + my, x + mx
            if 0 <= ny < N and 0 <= nx < M:
                new_maze[ny][nx] = max(new_maze[ny][nx], new_maze[y][x] + maze[ny][nx])

print(new_maze[N-1][M-1])

# Language : PyPy3
# Memory : 143088 KB
# Time : 316ms
# Time Complexity : O(N*M)