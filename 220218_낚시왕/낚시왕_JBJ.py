import collections, sys, heapq

MOVE = {1:(-1, 0), 2:(1, 0), 3:(0, 1), 4:(0, -1)}
CHANGE_DIRECTION = {1:2, 2:1, 3:4, 4:3}
SHARKS = dict()

R, C, M = map(int, sys.stdin.readline().strip().split())
for _ in range(M):
    r, c, speed, direction, size = map(int, sys.stdin.readline().strip().split())
    speed = speed % ((R-1) * 2) if direction <= 2 else speed % ((C-1) * 2) # speed optimization
    shark = {'size': size, 'speed': speed, 'direction': direction}
    SHARKS[(r-1, c-1)] = shark
    
total_sharks_size = 0  
for c in range(C):
    # 1. catch a shark
    for r in range(R):
        if (r, c) in SHARKS:
            total_sharks_size += SHARKS[(r, c)]['size']
            del SHARKS[(r, c)]
            break
    
    # 2. move sharks
    new_sharks = collections.defaultdict(list)
    for y, x in SHARKS:
        size, speed, direction = SHARKS[(y, x)].values()
        new_y, new_x = y, x
        dy, dx = MOVE[direction]
        
        while speed:
            if not(0 <= new_y+dy < R) or not(0 <= new_x+dx < C):
                direction = CHANGE_DIRECTION[direction]
                dy, dx = MOVE[direction]
            new_y, new_x = new_y+dy, new_x+dx
            speed-=1
        heapq.heappush(new_sharks[(new_y, new_x)], (-size, SHARKS[(y, x)]['speed'], direction))
        
    # 3. get the biggest sharks
    SHARKS = dict()
    for (new_y, new_x), shark_list in new_sharks.items():
        shark = {'size': -(shark_list[0][0]), 'speed': shark_list[0][1], 'direction': shark_list[0][2]}
        SHARKS[(new_y, new_x)] = shark
                
print(total_sharks_size)