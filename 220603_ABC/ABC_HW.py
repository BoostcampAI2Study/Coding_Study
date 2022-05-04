import sys
N, K = map(int, sys.stdin.readline().split())
dp = [[[[False] * (K + 1) for _ in range(N + 1)] for _ in range(N + 1)] for _ in range(N + 1)]
answer = [''] * N
def dfs(idx, a_cnt, b_cnt, k):
    if idx == N:
        return True if k == 0 else False
    if k < 0:
        return False
    if not dp[idx][a_cnt][b_cnt][k]:
        dp[idx][a_cnt][b_cnt][k] = True

        answer[idx] = 'A'
        if dfs(idx + 1, a_cnt + 1, b_cnt, k):
            return True
        answer[idx] = 'B'
        if dfs(idx + 1, a_cnt, b_cnt + 1, k - a_cnt):
            return True
        answer[idx] = 'C'
        if dfs(idx + 1, a_cnt, b_cnt, k - a_cnt - b_cnt):
            return True

    return False

print(''.join(answer)) if dfs(0, 0, 0, K) else print(-1)
