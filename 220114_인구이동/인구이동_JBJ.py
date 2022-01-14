import sys, collections 

N, left, right = map(int, sys.stdin.readline().strip().split())
A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]


def is_union(r, c):
    global N, A, is_visited
    union_set = set() # for unique elements usage purpose.

    Q = collections.deque()
    Q.append((r, c))
    is_visited[r][c] = True

    while Q:
        cur_r, cur_c = Q.popleft()

        # (right, left, down, up)
        for dr, dc in ((cur_r, cur_c+1), (cur_r, cur_c-1), (cur_r+1, cur_c), (cur_r-1, cur_c)):
            # possible indices check.
            if 0 <= dr < N and 0 <= dc < N:
                # given rule check.
                if left <= abs(A[cur_r][cur_c] - A[dr][dc]) <= right and not is_visited[dr][dc]:
                    is_visited[dr][dc] = True
                    union_set.add((cur_r, cur_c)) # duplicates OK. -> set()
                    union_set.add((dr, dc))
                    Q.append((dr, dc))
    
    # if there is a union.
    if union_set:
        # assign each country a new population number.
        new_population = sum([A[r][c] for r, c in union_set]) // len(union_set)
        for r, c in union_set:
            A[r][c] = new_population

        return True    
    return False


migration_days = 0
while True:
    is_visited = [[False]*N for _ in range(N)]
    union_exists = False
    
    for r in range(N):
        for c in range(N):
            if not is_visited[r][c] and is_union(r, c):
                union_exists = True

    if not union_exists:
        break

    migration_days += 1
        
print(migration_days)