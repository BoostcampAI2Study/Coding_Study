# https://www.acmicpc.net/problem/16940

from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

check_list = list(map(int, input().split()))


def bfs(check_list: list):
    q = deque([1])  # node
    visited = [False] * (N + 1)
    visited_order = []
    check_idx = 1
    while q:
        node = q.popleft()
        if visited[node]:
            continue
        visited[node] = True
        visited_order.append(node)

        # q에 넣을 후보군을 따로 저장
        tmp = defaultdict(int)
        for next_node in graph[node]:
            if not visited[next_node]:
                tmp[next_node] = 1

        # 후보군(tmp)중에 check list 다음 차례에 나와야하는 것들이 있는지 확인
        for i in range(len(tmp)):
            if tmp[check_list[check_idx + i]]:
                # 확인하고 있다면 queue에 넣음
                q.append(check_list[check_idx + i])
            else:
                # 없다면 check list는 BFS 탐색 순서가 틀린 것
                return False
        check_idx += len(tmp)
    return True


print(1 if bfs(check_list) else 0)
