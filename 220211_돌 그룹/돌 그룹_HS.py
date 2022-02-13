from collections import defaultdict
import sys

sys.setrecursionlimit(10000000)

A, B, C = list(map(int, input().split()))
visited = defaultdict(list)
def solution(a, b, c):
    if a == b == c:
        return 1
    if a > b and b not in visited[a]:
        visited[a].append(b)
        if solution(a-b, b+b, c):
            return 1
    if b > a and a not in visited[b]:
        visited[b].append(a)
        if solution(a+a, b-a, c):
            return 1
    if a > c and c not in visited[a]:
        visited[a].append(c)
        if solution(a-c, b, c+c):
            return 1
    if c > a and a not in visited[c]:
        visited[c].append(a)
        if solution(a+a, b, c-a):
            return 1
    if b > c and c not in visited[b]:
        visited[b].append(c)
        if solution(a, b-c, c+c):
            return 1
    if c > b and b not in visited[c]:
        visited[c].append(b)
        if solution(a, b+b, c-b):
            return 1

    return 0

if (A + B + C) % 3 != 0:
    print(0)
else:
    print(solution(A, B, C))

    
# Language        : Python3
# Memory          : 252676 KB
# Time            : 3900 ms
# Time complexity : ?