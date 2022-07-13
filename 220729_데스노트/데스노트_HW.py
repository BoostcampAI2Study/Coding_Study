import sys
sys.setrecursionlimit(10 ** 6)
N, M = map(int, sys.stdin.readline().split())
LENGTHS = [int(sys.stdin.readline()) for _ in range(N)]

dp = [-1] * N
def dfs(idx):
    if idx == N:
        return 0
    if dp[idx] != -1:
        return dp[idx]

    length, result = 0, 1e9
    for i in range(idx, N):
        length += LENGTHS[i]
        if length > M:
            break
        result = min(result, (M - length) ** 2 + dfs(i + 1)) if i != N - 1 else 0
        length += 1
    dp[idx] = result
    return result

print(dfs(0))
