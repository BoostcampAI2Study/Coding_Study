from collections import deque
N, K = map(int, input().split())
d = dict()
bfs = deque([[N, 0]])
d[N] = 0
while bfs:
    n, t = bfs[0]
    if n == K:
        print(t)
        break
    if n > 0:
        _t = d.get(n-1, -1)
        if _t == -1 or _t > t+1:
            bfs.append([n-1, t+1])
            d[n-1] = t+1
    if n < K:
        _t = d.get(n+1, -1)
        if _t == -1 or _t > t+1:
            bfs.append([n+1, t+1])
            d[n+1] = t+1
        _t = d.get(n*2, -1)
        if _t == -1 or _t > t+1:
            bfs.append([n*2, t+1])
            d[n*2] = t+1
    bfs.popleft()