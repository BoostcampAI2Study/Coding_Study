import sys

N, M = map(int, sys.stdin.readline().strip().split())
ROOMS = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
max_candies_room = [[0] * M for _ in range(N)] 

for y in range(N):
    for x in range(M):
        max_candies_cnt = 0
        for prev_y, prev_x in (y-1, x), (y, x-1), (y-1, x-1):
            if 0 <= prev_y < N and 0 <= prev_x < M:
                max_candies_cnt = max(max_candies_cnt, max_candies_room[prev_y][prev_x])
        max_candies_room[y][x] = ROOMS[y][x] + max_candies_cnt

print(max_candies_room[-1][-1])
        