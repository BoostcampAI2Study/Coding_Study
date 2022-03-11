import copy

def fish_and_direction(fishes, n=2):
    for idx in range(0, len(fishes), n):
        yield {'fish': fishes[idx], 'direction': fishes[idx+1]-1} 
# 0:↑, 1:↖, 2:←, 3:↙, 4:↓, 5:↘, 6:→, 7:↗
DIRECTIONS = {0:(-1, 0), 1:(-1, -1), 2:(0, -1), 3:(1, -1), 4:(1, 0), 5:(1, 1), 6:(0, 1), 7:(-1, 1)}
sea = [list(fish_and_direction(list(map(int, input().strip().split())))) for _ in range(4)]
max_fishes_sum = 0

def dfs(shark_y, shark_x, fishes_sum, sea):
    global max_fishes_sum, DIRECTIONS
    fishes_sum += sea[shark_y][shark_x]['fish']
    max_fishes_sum = max(max_fishes_sum, fishes_sum)
    sea[shark_y][shark_x]['fish'] = 0 # (shark: 0)
    coordinates = {sea[y][x]['fish']:(y, x) for y in range(4) for x in range(4) if sea[y][x]['fish'] > 0}

    # 1. fishes move
    for fish in range(1, 17):
        if fish not in coordinates: continue # already eaten
        y, x = coordinates[fish]
        direction = sea[y][x]['direction']

        while True:
            new_y, new_x = y+DIRECTIONS[direction][0], x+DIRECTIONS[direction][1]
            if 0 <= new_y < 4 and 0 <= new_x < 4 and (new_y, new_x) != (shark_y, shark_x):
                sea[y][x]['fish'], sea[new_y][new_x]['fish'],  = sea[new_y][new_x]['fish'], fish
                sea[y][x]['direction'], sea[new_y][new_x]['direction'] = sea[new_y][new_x]['direction'], direction
                coordinates[fish], coordinates[sea[y][x]['fish']] = (new_y, new_x), (y, x)
                break

            direction = (direction+1)%8 # rotate 45 degrees
            if direction == sea[y][x]['direction']: break

    # 2. shark eats
    direction = sea[shark_y][shark_x]['direction']

    for times in range(1, 5):
        new_shark_y = shark_y + (DIRECTIONS[direction][0] * times)
        new_shark_x = shark_x + (DIRECTIONS[direction][1] * times)
        if 0 <= new_shark_y < 4 and 0 <= new_shark_x < 4 and sea[new_shark_y][new_shark_x]['fish']:
            dfs(new_shark_y, new_shark_x, fishes_sum, copy.deepcopy(sea))

dfs(0, 0, 0, sea)
print(max_fishes_sum)
