import sys
from itertools import combinations
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

S = list(map(int, input().split()))

db = defaultdict(bool)

for k in range(1, N+1):
    for comb in list(combinations(S,k)):
        db[sum(comb)] = True



idx = 1

while 1:
    if db[idx] == False:
        print(idx)
        break
    else:
        idx += 1