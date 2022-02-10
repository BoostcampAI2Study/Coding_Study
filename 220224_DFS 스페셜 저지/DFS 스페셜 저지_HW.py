import sys

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    node1, node2 = map(int, input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)
visit_order = list(map(int, input().split()))
check = [False] * (N + 1)

# visit order이 1로 시작되어야 함
if visit_order[0] != 1:
    print(0)
    sys.exit()

# input으로 받은 정답 순서대로 딕셔너리 value 정렬
for i in range(1, N + 1):
    tree[i].sort(key=lambda x: visit_order.index(x))

# dfs
result = []
def dfs(x):
    global check, result
    if check[x] is True:
        return
    check[x] = True
    result.append(x)
    for node in tree[x]:
        dfs(node)

dfs(1)
print(1) if result == visit_order else print(0)
