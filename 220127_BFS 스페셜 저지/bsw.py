from collections import defaultdict
from collections import deque
from functools import cmp_to_key

N = int(input())

tree = defaultdict(list)
for _ in range(N-1):
    s, e = map(int, input().split())

    tree[s].append(e)
    tree[e].append(s)

q = deque([1])
visited = []

lst = list(map(int, input().split()))

def comp(a, b):
    return lst.index(a) - lst.index(b)


for k, v in tree.items():
    v.sort(key=cmp_to_key(comp))

while q:
    cur = q.popleft()

    if cur not in visited:

        for next in tree[cur]:
            q.append(next)

        visited.append(cur)

# print(tree)
# print(visited)

# print(sorted(tree[1], key=cmp_to_key(comp)))

if visited == lst:
    print(1)
else:
    print(0)
