import collections, sys

N = int(sys.stdin.readline().strip())
GRAPHS = collections.defaultdict(set)
for _ in range(N-1):
    n1, n2 = list(map(int, sys.stdin.readline().strip().split()))
    GRAPHS[n1].add(n2)
    GRAPHS[n2].add(n1)
BFS_ORDER = list(map(int, sys.stdin.readline().strip().split()))

def bfs():
    global BFS_ORDER, GRAPHS, N
    next_nodes_idx, queue, visited_nodes = 1, GRAPHS[1], set([1])

    # bfs feasibility check by given order.
    for node in BFS_ORDER[1:]:
        while not queue and next_nodes_idx < N: # update queue with next possible nodes.
            queue = GRAPHS[BFS_ORDER[next_nodes_idx]] - visited_nodes
            next_nodes_idx += 1

        if node in queue: # node is available.
            queue.remove(node)
            visited_nodes.add(node)
        else: # node is unavailable.
            return 0
    return 1

print(bfs())