# https://www.acmicpc.net/problem/2294

from collections import defaultdict, deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = set([int(input()) for _ in range(n)])
used_coin = [0] * (k + 1)

q = [(coin, 1) for coin in coins]

q = deque(q)
while q:
    value, used_coin_n = q.popleft()
    if value == k:
        print(used_coin_n)
        sys.exit()
    elif value > k:
        continue
    if used_coin[value]:
        continue
    used_coin[value] = 1
    for coin in coins:
        n_value = value + coin
        if n_value <= k and not used_coin[n_value]:
            q.append((n_value, used_coin_n + 1))
print(-1)
