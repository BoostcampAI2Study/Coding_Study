import collections, sys
sys.setrecursionlimit(10**7)
N = int(sys.stdin.readline().rstrip())
GRAPH = [[] for _ in range(N+1)]
is_cycled = [False]*(N+1)

for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    GRAPH[a].append(b)
    GRAPH[b].append(a)

def get_cycle(start_num, cur_num, cycle_cnt):
    global GRAPH, visited, is_cycled
    for adj_num in GRAPH[cur_num]:
        if adj_num == start_num and cycle_cnt >= 2: # cycle made.
            for n in range(1, N+1):
                if visited[n] == True:
                    is_cycled[n] = True
            return
        # first visit adjacent_num during start_num cycle and first edge between current_num and adjacent_num.
        if not visited[adj_num] and not (is_cycled[cur_num] and is_cycled[adj_num]):
            visited[adj_num] = True
            get_cycle(start_num, adj_num, cycle_cnt+1)
            visited[adj_num] = False

for num in range(1, N+1):
    visited = [False] * (N+1)
    visited[num] = True
    get_cycle(num, num, 0)

# get minimum distances
Q, distances = collections.deque(), [-1]*(N+1)
for num in range(1, N+1):
    if is_cycled[num]: # cycle num is initialized with 0 distance.
        distances[num] = 0
        Q.append(num)
# bfs
while Q: 
    cur_num = Q.popleft()
    for adj_num in GRAPH[cur_num]:
        if distances[adj_num] == -1:
            distances[adj_num] = distances[cur_num]+1
            Q.append(adj_num)

print(' '.join(map(str, distances[1:])))