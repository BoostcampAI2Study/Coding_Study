import collections, sys

def bfs():
    BOARD = [sys.stdin.readline().strip() for _ in range(8)]
    WALLS = dict()

    # All of the moving walls cases for all-time steps.
    WALLS[0] = set((y, x) for y in range(8) for x in range(8) if BOARD[y][x] == '#')
    for idx in range(1, 8):
        next_time_step_walls = set((wall[0]+1, wall[1]) for wall in WALLS[idx-1] if wall[0]+1 < 8)
        if not next_time_step_walls: break
        WALLS[idx] = next_time_step_walls
    
    MAX_TIME_STEP = len(WALLS)-1
    Q = collections.deque()
    Q.append((7, 0, 0)) # Uk Jae start point & time_step => (y, x, time_step)
    while Q:
        y, x, time_step = Q.popleft()

        if (y, x) == (0, 7) or time_step > MAX_TIME_STEP: return 1
        
        for new_y, new_x in (y, x), (y, x+1), (y, x-1), (y+1, x), (y-1, x), (y+1, x+1), (y-1, x-1), (y+1, x-1), (y-1, x+1):
            # 1. Uk Jae moves.
            if 0 <= new_y < 8 and 0 <= new_x < 8 and (new_y, new_x) not in WALLS[time_step]:
                # 2. move walls.
                if time_step+1 > MAX_TIME_STEP or (time_step < MAX_TIME_STEP and (new_y, new_x) not in WALLS[time_step+1]):
                    Q.append([new_y, new_x, time_step+1])
    return 0

print(bfs())