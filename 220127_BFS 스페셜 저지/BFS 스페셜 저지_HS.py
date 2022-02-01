from collections import defaultdict, deque
import sys

N = int(input())
# Visiting Test
visited = [0 for _ in range(N+1)]
visited[1] = 1
# Node connection relationship
link = defaultdict(list)

for i in range(N-1):
    a, b = list(map(int, input().split()))
    link[a].append(b)
    link[b].append(a)
# Input order
bfs = list(map(int, input().split()))
# Exception
if bfs[0] != 1:
    print(0)
    sys.exit()
# Test function for correct answers
def check_order():
    idx = 1
    # preset = present Node
    for present in bfs:
        children = []
        # child = child Node
        for child in link[present]:
            # Whether to visit
            if not visited[child]:
                visited[child] = 1
                children.append(child)
        # Approach with index
        if children and (sorted(children) != sorted(bfs[idx:idx+len(children)])):
            return 0
        
        idx += len(children)

    return 1

print(check_order())

# Language : pypy3 / python3
# Memory : 180640 kb / 64996 kb
# time 580 ms / 4720 ms
# time complexity : 모르겠음