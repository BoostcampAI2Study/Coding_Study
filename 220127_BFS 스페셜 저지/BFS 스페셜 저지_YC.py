from collections import deque, defaultdict

def bfs():
    visited = [False] * (N+1)
    queue = deque()
    queue.append(1)
    visited[1] = True

    idx = 1
    while queue:
        x = queue.popleft()
        children = []

        for node in GRAPH[x]:
            if not visited[node]:
                children.append(node)

        if sorted(answer[idx:idx+len(children)]) == sorted(children):
            for child in answer[idx:idx+len(children)]:
                queue.append(child)
                visited[child] = True
            idx +=len(children)
        else:
            return 0
              
    return 1

GRAPH = defaultdict(list)

N = int(input())
for _ in range(N-1):
    start, end = map(int, input().split())
    GRAPH[start].append(end)
    GRAPH[end].append(start)

answer = list(map(int, input().split()))

if answer[0] == 1:
    print(bfs())
else:
    print(0)
