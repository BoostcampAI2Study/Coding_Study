import collections, itertools, sys

N, M = map(int, sys.stdin.readline().rstrip().split())
LAB = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

TO_FILL = 0
VIRUS_CANDIDATES, TO_FILL = set(), 0 # spaces except for the walls.
for y in range(N):
    for x in range(N):
        if LAB[y][x] != 1:
            TO_FILL += 1
            if LAB[y][x] == 2:
                VIRUS_CANDIDATES.add((y, x))

min_spread_time = 1e4
for viruses in itertools.combinations(VIRUS_CANDIDATES, M):
    visited, filled_cnt = [[False]*N for _ in range(N)], M
    
    Q = collections.deque()
    for y, x in viruses:
        Q.append((y, x, 0))
        visited[y][x] = True
    
    while Q:
        y, x, spread_time = Q.popleft()
        for new_y, new_x in (y+1, x), (y-1, x), (y, x+1), (y, x-1):
            if 0 <= new_y < N and 0 <= new_x < N and LAB[new_y][new_x] != 1 and not visited[new_y][new_x]:
                visited[new_y][new_x] = True
                filled_cnt += 1
                Q.append((new_y, new_x, spread_time+1))
    
    if min_spread_time > spread_time and filled_cnt == TO_FILL: 
        min_spread_time = spread_time

print(min_spread_time if min_spread_time != 1e4 else -1)