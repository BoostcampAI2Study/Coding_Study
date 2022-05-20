# https://www.acmicpc.net/problem/2252

from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)
edge_cnt = defaultdict(int)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    edge_cnt[b] += 1

q = deque([])
answer = []
for i in range(1, N + 1):
    if edge_cnt[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    answer.append(str(node))
    for next_node in graph[node]:
        edge_cnt[next_node] -= 1
        if not edge_cnt[next_node]:
            q.append(next_node)

print(" ".join(answer))
