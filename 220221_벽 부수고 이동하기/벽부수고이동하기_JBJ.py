import collections, sys

N, M= map(int, sys.stdin.readline().strip().split())
MAP = [sys.stdin.readline().strip() for _ in range(N)]

def bfs():
    global N, M, MAP
    Q = collections.deque()
    min_distances = [[[-1] * (M) for _ in range(N)] for _ in range(2)] # speed optimization: (2, N, M) -> (N, M, 2)
    
    Q.append((0, 0, 0))          # broken wall, y, x
    min_distances[0][0][0] = 1   # broken wall, N, M

    while Q:
        broken_wall, y, x = Q.popleft()

        if y == N-1 and x == M-1:
            return min_distances[broken_wall][y][x]

        for new_y, new_x in (y, x+1), (y, x-1), (y+1, x), (y-1, x):
            if 0 <= new_y < N and 0 <= new_x < M:
                if MAP[new_y][new_x] == '1': # wall exists and no broken wall → break wall
                    if not broken_wall and min_distances[broken_wall+1][new_y][new_x] == -1:
                        min_distances[broken_wall+1][new_y][new_x] = min_distances[broken_wall][y][x]+1
                        Q.append((broken_wall+1, new_y, new_x))
                else: # no wall
                    if min_distances[broken_wall][new_y][new_x] == -1:
                        min_distances[broken_wall][new_y][new_x] = min_distances[broken_wall][y][x]+1
                        Q.append((broken_wall, new_y, new_x))
    return -1

print(bfs())