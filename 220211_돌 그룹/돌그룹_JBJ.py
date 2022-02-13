import collections, sys

A, B, C = map(int, sys.stdin.readline().strip().split())
TOTAL_ROCKS, answer = A+B+C, 0
min_max_visited = [[False]*(TOTAL_ROCKS+1) for _ in range(TOTAL_ROCKS+1)]

if (TOTAL_ROCKS) % 3 == 0: # possible to equally distribute
    Q = collections.deque()
    Q.append((min(A, B, C), max(A, B, C))) # only focus on min & max groups
    
    while Q: # group_min <= group_mid <= group_max
        group_min, group_max = Q.popleft()
        group_mid = TOTAL_ROCKS-(group_min+group_max) # mid group is calculated by min & max groups
        
        if group_min == group_mid == group_max:
            answer = 1
            break
        
        for x, y in (group_min, group_max), (group_min, group_mid), (group_mid, group_max):
            if x == y: continue
            # pick two groups with different size, x < y, x = x+x, y = y-x
            y -= x
            x *= 2
            remains = TOTAL_ROCKS-(x+y)

            new_group_min = min(x, y, remains)
            new_group_max = max(x, y, remains)
            if not min_max_visited[new_group_min][new_group_max]:
                Q.append((new_group_min, new_group_max))
                min_max_visited[new_group_min][new_group_max] = True # visited check
                    
print(answer) 