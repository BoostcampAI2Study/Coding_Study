import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
LADDERS_OR_SNAKES = [0]*101
for _ in range(N+M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    LADDERS_OR_SNAKES[x] = y

cur_locations, dice_roll_cnt, visited = [1], 0, [False]*101
while not visited[100]:
    next_locations = []

    while cur_locations:
        cur_location = cur_locations.pop()
        for next_location in range(cur_location+1, cur_location+7):
            if next_location <= 100 and not visited[next_location]:
                visited[next_location] = True
                while LADDERS_OR_SNAKES[next_location]:
                    next_location = LADDERS_OR_SNAKES[next_location]
                    visited[next_location] = True
                next_locations.append(next_location)
    
    cur_locations = next_locations
    dice_roll_cnt += 1
print(dice_roll_cnt)