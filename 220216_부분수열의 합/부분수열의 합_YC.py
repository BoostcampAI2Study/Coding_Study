from itertools import combinations

N = int(input())

S = list(map(int, input().split()))
check = [False for _ in range(sum(S)+2)]
check[0] = True
S.sort()

for i in range(1, N+1):
    lst = list(combinations(S,i))
    for l in lst:
        check[sum(l)] = True

for i, c in enumerate(check):
    if not c:
        print(i)
        break