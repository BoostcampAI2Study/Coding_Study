import sys
SONGS = list(map(int, sys.stdin.readline().split()))
dp = [[[[-1] * 51 for _ in range(51)] for _ in range(51)] for _ in range(51)]

def dfs(s, a, b, c):
    if s == 0:
        return 1 if a == 0 and b == 0 and c == 0 else 0
    if a < 0 or b < 0 or c < 0:
        return 0
    if dp[s][a][b][c] > -1:
        return dp[s][a][b][c]

    cnt = dfs(s - 1, a - 1, b, c)
    cnt += dfs(s - 1, a, b - 1, c)
    cnt += dfs(s - 1, a, b, c - 1)
    cnt += dfs(s - 1, a - 1, b - 1, c)
    cnt += dfs(s - 1, a - 1, b, c - 1)
    cnt += dfs(s - 1, a, b - 1, c - 1)
    cnt += dfs(s - 1, a - 1, b - 1, c - 1)
    dp[s][a][b][c] = cnt
    return cnt

print(dfs(SONGS[0], SONGS[1], SONGS[2], SONGS[3]) % 1000000007)
