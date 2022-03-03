import collections, sys

N, M = map(int, sys.stdin.readline().strip().split())
MAP = [sys.stdin.readline().strip().split() for _ in range(N)]

safe_distances = [[0 if MAP[y][x] == '1' else 50 for x in range(M)] for y in range(N)]
Q = collections.deque()
Q.extend([(y, x, 0) for y in range(N) for x in range(M) if MAP[y][x] == '1'])

while Q:
    y, x, safe_distance = Q.popleft()
    
    for new_y, new_x in (y, x+1), (y, x-1), (y+1, x), (y-1, x), (y+1, x+1), (y-1, x-1), (y+1, x-1), (y-1, x+1):
        if 0 <= new_y < N and 0 <= new_x < M and MAP[new_y][new_x] == '0':
            if safe_distance+1 < safe_distances[new_y][new_x]:
                safe_distances[new_y][new_x] = safe_distance+1
                Q.append((new_y, new_x, safe_distance+1))

print(max(map(max, safe_distances)))