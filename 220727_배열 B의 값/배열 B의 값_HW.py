import sys
N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

raws_sum = [0] * N
for r in range(N):
    for c in range(M):
        raws_sum[r] += A[r][c] if c == 0 or c == M - 1 else A[r][c] * 2

cols_sum = [0] * M
for c in range(M):
    for r in range(N):
        cols_sum[c] += A[r][c] if r == 0 or r == N - 1 else A[r][c] * 2

raw_total_sum, col_total_sum = sum(raws_sum) * 2, sum(cols_sum) * 2
result = raw_total_sum - raws_sum[0] - raws_sum[N - 1]
for r in range(1, N - 1):
    result = max(result, raw_total_sum - raws_sum[0] - raws_sum[r])
    result = max(result, raw_total_sum - raws_sum[N - 1] - raws_sum[r])
for c in range(1, M - 1):
    result = max(result, col_total_sum - cols_sum[0] - cols_sum[c])
    result = max(result, col_total_sum - cols_sum[M - 1] - cols_sum[c])

print(result)
