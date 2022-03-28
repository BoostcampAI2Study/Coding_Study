import collections, itertools, sys, copy

N, M = map(int, sys.stdin.readline().rstrip().split())
MAP = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
answer = 0

EMPTY_SPACE_SET, VIRUS_SET = set(), set()
for y in range(N):
    for x in range(M):
        if MAP[y][x] == 0:
            EMPTY_SPACE_SET.add((y, x))
        elif MAP[y][x] == 2:
            VIRUS_SET.add((y, x))

def get_safe_zone_size(map_, empty_spaces):
    global MAP, N, M, VIRUS_SET
    for y, x in empty_spaces: # build 3 walls
        map_[y][x] = 1
    
    Q = collections.deque(VIRUS_SET) # spread viruses
    while Q:
        y, x = Q.popleft()
        for new_y, new_x in (y+1, x), (y-1, x), (y, x+1), (y, x-1):
            if 0 <= new_y < N and 0 <= new_x < M and map_[new_y][new_x] == 0:
                map_[new_y][new_x] = 2
                Q.append((new_y, new_x))

    safe_zone_cnt = 0
    for row in map_:
        safe_zone_cnt += row.count(0)
    return safe_zone_cnt
    
for empty_spaces in itertools.combinations(EMPTY_SPACE_SET, 3):
    answer = max(answer, get_safe_zone_size(copy.deepcopy(MAP), empty_spaces))
print(answer)