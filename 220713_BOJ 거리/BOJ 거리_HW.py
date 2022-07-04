import sys
N = int(sys.stdin.readline())
LETTERS = list(sys.stdin.readline().strip())

dp = [1e9] * N
dp[0] = 0
for cur_idx in range(N):
    for next_idx in range(cur_idx + 1, N):
        if (LETTERS[cur_idx] == 'B' and LETTERS[next_idx] == 'O') or (LETTERS[cur_idx] == 'O' and LETTERS[next_idx] == 'J') or (LETTERS[cur_idx] == 'J' and LETTERS[next_idx] == 'B'):
            dp[next_idx] = min(dp[next_idx], dp[cur_idx] + (next_idx - cur_idx) ** 2)

print(dp[N - 1]) if dp[N - 1] != 1e9 else print(-1)
