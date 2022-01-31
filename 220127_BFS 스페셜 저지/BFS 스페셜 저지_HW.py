import collections
import sys

N = int(input())
tree_input = [map(int, input().split()) for _ in range(N - 1)]
answer_order = list(map(int, input().split()))
visit = [False] * (N + 1)

# key - value: 서로 연결되어 있는 노드
tree_info = collections.defaultdict(list)
for node1, node2 in tree_input:
    tree_info[node1].append(node2)
    tree_info[node2].append(node1)

# 1부터 시작하는지 확인
if answer_order[0] != 1:
    print(0)
    sys.exit()

# input으로 받은 정답 순서대로 딕셔너리 value 정렬
for i in range(1, N + 1):
    tree_info[i].sort(key=lambda x: answer_order.index(x))

# BFS
q = collections.deque()
q.append(1)
visit[1] = True
result = [1]
while q:
    node = q.popleft()
    adjacency_nodes = tree_info[node]
    # 방문하지 않은 자식 result 저장 + 큐에 넣기
    for adj_node in adjacency_nodes:
        if visit[adj_node] is False:
            result.append(adj_node)
            q.append(adj_node)
            visit[adj_node] = True

print(1) if result == answer_order else print(0)
