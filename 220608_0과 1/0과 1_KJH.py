# https://www.acmicpc.net/problem/8111
from math import log
from collections import deque
import sys

input = sys.stdin.readline

N = int(input())


def bfs(num):
    q = deque([1])
    visited = [0] * num
    while q:
        n = q.popleft()
        for i in range(2):
            tmp = (n * 10 + i) % num
            if not visited[tmp]:
                if tmp == 0:
                    return n * 10 + i
                visited[tmp] = 1
                q.append(n * 10 + i)
        if log(n, 10) > 100:
            return "BRAK"
    return "BRAK"


for _ in range(N):
    print(bfs(int(input())))
