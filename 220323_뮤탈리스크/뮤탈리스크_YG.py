import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline

# Input
N = int(input())
scvs = list(map(int, input().split()))

while len(scvs) < 3:
    scvs.append(0)

attack = [9,3,1]

q = deque()

q.append((scvs[0], scvs[1], scvs[2], 0))

visited = [[[False for _ in range(61)] for _ in range(61)] for _ in range(61)]

perm = list(permutations([9, 3, 1], 3))

answer = 1e9
while q:
    a, b, c, cnt = q.popleft()

    if a == b == c == 0:
        print(cnt)
        break

    # 파괴
    for p1, p2, p3 in perm:
        na, nb, nc = a-p1, b-p2, c-p3
        if na < 0:
            na = 0
        if nb < 0:
            nb = 0
        if nc < 0:
            nc = 0
        if visited[na][nb][nc] == False:
            visited[na][nb][nc] = True
            q.append((na, nb, nc, cnt+1))
