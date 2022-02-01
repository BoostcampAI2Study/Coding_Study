import itertools

N, S = map(int, input().split())
sequence = list(map(int, input().split()))
cnt = 0

for k in range(1, N+1):
    subsequences = itertools.combinations(range(0,N),k)
    for subsequence in subsequences:
        total = 0
        for element in subsequence:
            total += sequence[element]
        if total == S:
            cnt += 1
print(cnt)