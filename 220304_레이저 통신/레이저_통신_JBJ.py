import collections, sys

W, H = map(int, sys.stdin.readline().strip().split())
MAP = [sys.stdin.readline().strip() for _ in range(H)]
C1, C2 = [(y, x) for y in range(H) for x in range(W) if MAP[y][x] == 'C']

Q = collections.deque()
Q.append([-1, C1[0], C1[1], -1]) # mirror count, height, width, direction 

min_mirror_cnts = [[sys.maxsize]*W for _ in range(H)]
min_mirror_cnts[C1[0]][C1[1]] = 0
while Q:
    mirror_cnt, y, x, direction = Q.popleft()
    for new_direction, (new_y, new_x) in enumerate(((y, x+1), (y, x-1), (y+1, x), (y-1, x))): # (right:0, left:1, down:2, up:3)
        if 0 <= new_y < H and 0 <= new_x < W and MAP[new_y][new_x] != '*':
            new_mirror_cnt = mirror_cnt+1 if new_direction != direction else mirror_cnt
            if min_mirror_cnts[new_y][new_x] >= new_mirror_cnt: # consider equal cases not to lose possible cases
                min_mirror_cnts[new_y][new_x] = new_mirror_cnt
                Q.append([min_mirror_cnts[new_y][new_x], new_y, new_x, new_direction])
                
print(min_mirror_cnts[C2[0]][C2[1]])