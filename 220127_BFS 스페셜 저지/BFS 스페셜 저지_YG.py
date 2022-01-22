from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

target = list(map(int, input().split()))

if target[0] != 1:
    print(0)
    sys.exit()

visited = [False]*(N+1)
visited[1] = True

q = deque()
q.append(1)

idx = 1

while q:
    now = q.popleft()

    nq = []
    for v in graph[now]:
        if visited[v] == False:
            visited[v] = True
            nq.append(v)
    l = len(nq)


    if sorted(nq) != sorted(target[idx:idx+l]):
        print(0)
        sys.exit()

    for k in range(idx, idx+l):
        q.append(target[k])

    idx += l

print(1)
