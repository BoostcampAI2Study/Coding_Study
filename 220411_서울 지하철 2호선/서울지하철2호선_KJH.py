# https://www.acmicpc.net/problem/16947

from collections import defaultdict, deque
import sys

sys.setrecursionlimit(10 ** 6)


input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N + 1)
cycle = []


def find_cycle(node, prev):
    global visited, cycle

    if visited[node] == 1:
        return node
    visited[node] = 1
    for i in graph[node]:
        if i != prev:
            point = find_cycle(i, node)
            if point > -1:
                visited[node] = 2
                cycle.append(node)
                if point != node:
                    return point
                else:
                    return -1
    return -1


find_cycle(1, 1)
answer = []
distance = [0 if visited[i] == 2 else float("inf") for i in range(N + 1)]

q = deque(cycle)
while q:
    node = q.popleft()
    for i in graph[node]:
        if distance[node] + 1 < distance[i]:
            distance[i] = distance[node] + 1
            q.append(i)
print(*distance[1:])

