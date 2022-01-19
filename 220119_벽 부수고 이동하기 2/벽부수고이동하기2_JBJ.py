import collections, sys

N, M, K = map(int, sys.stdin.readline().strip().split())
MAP = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]

def bfs():
    global N, M, K, MAP
    Q = collections.deque()
    min_distances = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
    
    Q.append((0, 0, 0))          # y, x, broken walls count
    min_distances[0][0][0] = 1   # N, M, K

    while Q:
        y, x, broken_walls = Q.popleft()

        if y == N-1 and x == M-1:
            return min_distances[y][x][broken_walls]

        for new_y, new_x in ((y, x+1), (y, x-1), (y+1, x), (y-1, x)):
            if 0 <= new_y < N and 0 <= new_x < M:
                # wall exists and K count remains. → break wall
                if MAP[new_y][new_x] and broken_walls < K and not min_distances[new_y][new_x][broken_walls]:
                    min_distances[new_y][new_x][broken_walls+1] = min_distances[y][x][broken_walls] + 1
                    Q.append((new_y, new_x, broken_walls+1))
                # no wall
                elif not MAP[new_y][new_x] and not min_distances[new_y][new_x][broken_walls]:
                    min_distances[new_y][new_x][broken_walls] = min_distances[y][x][broken_walls] + 1
                    Q.append((new_y, new_x, broken_walls))
    return -1

print(bfs())