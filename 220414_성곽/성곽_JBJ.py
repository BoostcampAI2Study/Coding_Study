import collections, sys

def bitmasking(num):
    num = int(num)
    wall_to_the_south = '1' if num & (1 << 3) == 8 else '0'
    wall_to_the_east = '1' if num & (1 << 2) == 4 else '0'
    wall_to_the_north = '1' if num & (1 << 1) == 2 else '0'
    wall_to_the_west = '1' if num & 1 == 1 else '0'
    return wall_to_the_south + wall_to_the_east + wall_to_the_north + wall_to_the_west

N, M = map(int, sys.stdin.readline().rstrip().split())
MAP = [list(map(bitmasking, sys.stdin.readline().rstrip().split())) for _ in range(M)]
MOVE_DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)] # south, east, north, west
visited = [[-1]*N for _ in range(M)]
rooms, room_num = list(), 0

def bfs(y, x, room_num):
    global visited, N, M, MAP

    room_size = 1
    Q = collections.deque([(y, x)]) # y, x
    while Q:
        y, x = Q.popleft()
        for idx in range(4):
            new_y, new_x = y+MOVE_DIRECTIONS[idx][0], x+MOVE_DIRECTIONS[idx][1]
            if MAP[y][x][idx] == '0' and 0 <= new_y < M and 0 <= new_x < N and visited[new_y][new_x] == -1: # wall doesn't exist.
                visited[new_y][new_x] = room_num
                room_size += 1
                Q.append((new_y, new_x))

    return room_size

for y in range(M): # count rooms and get the biggest room size.
    for x in range(N):
        if visited[y][x] == -1:
            visited[y][x] = room_num
            rooms.append(bfs(y, x, room_num))
            room_num += 1
print(len(rooms))
max_room_size = max(rooms)
print(max_room_size)

already_checked_walls = set() # get the biggest room size after wall elimination.
for y in range(M):
    for x in range(N):
        for idx in range(4):
            if (y, x, idx) in already_checked_walls: continue

            new_y, new_x = y+MOVE_DIRECTIONS[idx][0], x+MOVE_DIRECTIONS[idx][1]
            if MAP[y][x][idx] == '1' and 0 <= new_y < M and 0 <= new_x < N and visited[y][x] != visited[new_y][new_x]: # wall exists.
                already_checked_walls.add((new_y, new_x, (idx+2)%4))
                max_room_size = max(max_room_size, rooms[visited[y][x]] + rooms[visited[new_y][new_x]])
print(max_room_size)