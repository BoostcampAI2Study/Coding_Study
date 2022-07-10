import sys, itertools
N, L, R, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

A.sort()
cnt = 0
for i in range(2, N + 1):
    for sequence in itertools.combinations(A, i):
        level_sum = sum(sequence)
        if L <= level_sum <= R and sequence[-1] - sequence[0] >= X:
            cnt += 1
print(cnt)
