import sys, collections

N, M = map(int, sys.stdin.readline().rstrip().split())
MAP = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
C_COORDINATES = []
for y in range(N):
    for x in range(M):
        if MAP[y][x] == 'S':
            S_COORDINATE = (y, x)
        if MAP[y][x] == 'C':
            C_COORDINATES.append((y, x))

def bfs():
    global N, M, MAP, S_COORDINATE, C_COORDINATES

    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)] # right, left, down, up
    Q = collections.deque([(S_COORDINATE[0], S_COORDINATE[1], -1, 0, 0)])
    is_visited = [[[[False]*M for _ in range(N)] for _ in range(4)] for _ in range(3)]# (C_BITS, DIRECTIONS, N, M)
    while Q:
        cur_y, cur_x, prev_direction, time_cnt, c_bits = Q.popleft()

        for c_idx in range(2):
            if C_COORDINATES[c_idx] == (cur_y, cur_x):
                if c_bits == (c_idx+1): continue
                elif (c_bits | (c_idx+1)) == 3: return time_cnt
                elif c_bits == 0: c_bits |= (c_idx+1)

        for direction in range(4):
            if prev_direction == direction: continue

            new_y, new_x = cur_y+DIRECTIONS[direction][0], cur_x+DIRECTIONS[direction][1]
            if 0 <= new_y < N and 0 <= new_x < M and MAP[new_y][new_x] != '#' and not is_visited[c_bits][direction][cur_y][cur_x]:
                is_visited[c_bits][direction][cur_y][cur_x] = True
                Q.append((new_y, new_x, direction, time_cnt+1, c_bits))
    return -1

print(bfs())