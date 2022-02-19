import collections, sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline().strip())
GRAPH = collections.defaultdict(set)
for _ in range(N-1):
    node_1, node_2 = map(int, sys.stdin.readline().strip().split())
    GRAPH[node_1].add(node_2)
    GRAPH[node_2].add(node_1)
dfs_order = collections.deque(list(map(int, sys.stdin.readline().strip().split())))

def dfs(node):
    global dfs_order
    while dfs_order and dfs_order[0] in GRAPH[node]:
        next_node = dfs_order.popleft()
        dfs(next_node)

if dfs_order[0] == 1:
    start_node = dfs_order.popleft()
    dfs(start_node)

print(1 if len(dfs_order) == 0 else 0)