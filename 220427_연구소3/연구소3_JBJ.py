import collections, itertools, sys

N, M = map(int, sys.stdin.readline().rstrip().split())
LAB = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

VIRUS_CANDIDATES, TO_FILL = set(), 0 # spaces except for the walls.
for y in range(N):
    for x in range(N):
        if LAB[y][x] != 1:
            TO_FILL += 1
            if LAB[y][x] == 2:
                VIRUS_CANDIDATES.add((y, x))

answer = 1e5
for viruses in itertools.combinations(VIRUS_CANDIDATES, M):
    visited, filled_cnt, min_spread_time = [[False]*N for _ in range(N)], M, 0
    deactivated_viruses = VIRUS_CANDIDATES - set(viruses)
    
    Q = collections.deque()
    for y, x in viruses:
        Q.append((y, x, 0))
        visited[y][x] = True
    
    while Q:
        y, x, spread_time = Q.popleft()

        if (y, x) not in deactivated_viruses: # deactivated viruses' spread time does not count.
            min_spread_time = spread_time

        for new_y, new_x in (y+1, x), (y-1, x), (y, x+1), (y, x-1):
            if 0 <= new_y < N and 0 <= new_x < N and LAB[new_y][new_x] != 1 and not visited[new_y][new_x]:
                visited[new_y][new_x] = True
                filled_cnt += 1
                Q.append((new_y, new_x, spread_time+1))
    
    if filled_cnt == TO_FILL:
        answer = min(answer, min_spread_time)
        
print(answer if answer != 1e5 else -1)