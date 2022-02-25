import collections, sys

N, M, K = map(int, sys.stdin.readline().strip().split())
MAP = [sys.stdin.readline().strip() for _ in range(N)]

def bfs():
    global N, M, K, MAP
    Q = collections.deque()
    min_distances = [[[-1]*M  for _ in range(N)] for _ in range(K+1)]
    
    Q.append((0, 0, 0, 1))       # broken walls count, y, x, distances
    min_distances[0][0][0] = 1   # K, N, M

    while Q:
        broken_walls, y, x, distances = Q.popleft()

        if y == N-1 and x == M-1:
            return min_distances[broken_walls][y][x]

        for new_y, new_x in (y, x+1), (y, x-1), (y+1, x), (y-1, x):
            if 0 <= new_y < N and 0 <= new_x < M:
                # wall exists and K count remains. 
                if MAP[new_y][new_x] == '1' and broken_walls < K and min_distances[broken_walls+1][new_y][new_x] == -1:
                    if distances % 2 == 0: # night: wait until day comes.
                        Q.append((broken_walls, y, x, distances+1))
                    else: # day: break wall.
                        min_distances[broken_walls+1][new_y][new_x] = distances + 1
                        Q.append((broken_walls+1, new_y, new_x, distances+1))
                # no wall.
                elif MAP[new_y][new_x] == '0' and min_distances[broken_walls][new_y][new_x] == -1:
                    min_distances[broken_walls][new_y][new_x] = distances + 1
                    Q.append((broken_walls, new_y, new_x, distances+1))
    return -1

print(bfs())