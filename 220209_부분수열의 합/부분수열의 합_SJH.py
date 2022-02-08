from sys import stdin
from itertools import combinations

input = stdin.readline
N, S = map(int, input().split())

nums = list(map(int, input().split()))
answer = 0

for n in range(N, 0, -1):
    for combi in combinations(nums, n):
        total = sum(combi)

        if total == S:
            answer += 1

print(answer)