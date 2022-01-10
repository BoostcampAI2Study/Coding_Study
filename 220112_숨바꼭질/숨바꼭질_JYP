import sys
from collections import deque

n, k = map(int, input().split())
q = deque()
q.append(n)
dp = [0] * 100001

def bfs():
    while q:
        s = q.popleft()
        if s == k:
            return dp[k]
        for nx in (s - 1, s + 1, s * 2):
            if 0 <= nx <= 100000 and not dp[nx]:
                dp[nx] = dp[s] + 1
                q.append(nx)

print(bfs())
