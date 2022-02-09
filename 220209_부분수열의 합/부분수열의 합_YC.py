from itertools import combinations

N, S = map(int, input().split())

A = list(map(int, input().split()))
cnt=0

for i in range(1, N+1):
    lst = list(combinations(A,i))
    for l in lst:
        if sum(l) == S:
            cnt+=1
print(cnt)