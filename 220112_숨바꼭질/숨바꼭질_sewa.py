import sys
from collections import deque


def BFS(root, destination):
    q = deque([root])
    d = [0] * 100001
    # print(q)
    while q:
        l = q.popleft()
        # print(q, l)
        if l == destination:
            return d[l]
        else :     
            for v in [l-1, l+1, 2 * l]:
                # print(v)
                if not d[v] and 0<= v <= 100000:
                    d[v] = d[l]+1
                    q.append(v)


N, K = map(int, sys.stdin.readline().split())
print(BFS(N, K)) 