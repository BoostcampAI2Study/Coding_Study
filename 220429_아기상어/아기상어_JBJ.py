import collections

BABY_SHARK = -1
N, MAP = int(input().rstrip()), []
for y in range(N):
    row_spaces = list(map(int, input().rstrip().split()))
    MAP.append(row_spaces)
    for x, space in enumerate(row_spaces):
        if space == 9:
            MAP[y][x] = 0
            BABY_SHARK = (y, x, 2) # y_coordinate, x_coordinate, shark_size

eaten_fishes_cnt, total_time = 0, 0
def baby_shark_eats_fish(baby_shark_y, baby_shark_x, baby_shark_size):
    global N, MAP, eaten_fishes_cnt

    visited, min_taken_time, fish_candidates = [[False]*N for _ in range(N)], 1e9, list()
    visited[baby_shark_y][baby_shark_x] = True

    Q = collections.deque([(baby_shark_y, baby_shark_x, 0)])
    while Q:
        y, x, taken_time = Q.popleft()
        
        if min_taken_time < taken_time: continue

        if 0 < MAP[y][x] < baby_shark_size:
            min_taken_time = min(min_taken_time, taken_time)
            fish_candidates.append((y, x, taken_time))
            
        for new_y, new_x in (y, x-1), (y-1, x), (y, x+1), (y+1, x): # left, up, right, down
            if 0 <= new_y < N and 0 <= new_x < N and not visited[new_y][new_x] and MAP[new_y][new_x] <= baby_shark_size:
                visited[new_y][new_x] = True
                Q.append((new_y, new_x, taken_time+1))

    if fish_candidates:
        y, x, taken_time = sorted(fish_candidates)[0] # get the minimum taken time fish on the top left corner to eat.
        MAP[y][x] = 0
        eaten_fishes_cnt += 1
        if eaten_fishes_cnt == baby_shark_size:
            baby_shark_size += 1
            eaten_fishes_cnt = 0
        return (y, x, baby_shark_size, taken_time)
    else: # no fish candidates.
        return -1

while True:
    return_value = baby_shark_eats_fish(BABY_SHARK[0], BABY_SHARK[1], BABY_SHARK[2])
    if return_value == -1:
        print(total_time)
        break
    else:
        BABY_SHARK = (return_value[0], return_value[1], return_value[2])
        total_time += return_value[3]