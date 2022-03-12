# 1 2 0 1 3 2 1 5 4 2
# 0 1 2 2 3 4 4 4 5 5
import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0] + [sys.maxsize]*(N-1)

for idx in range(N):
    max_jump_cnt = A[idx]
    for next_idx in range(idx+1, idx+max_jump_cnt+1):
        if next_idx >= N: break
        dp[next_idx] = min(dp[next_idx], dp[idx]+1)

print(dp[-1] if dp[-1] != sys.maxsize else -1)