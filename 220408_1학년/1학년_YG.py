import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

dp = [[0]*21 for _ in range(N-1)]

dp[0][arr[0]] = 1

for k in range(1, N-1):
    for idx in range(21):
        if dp[k-1][idx]:
            for next_number in [arr[k], -arr[k]]:
                if 0 <= idx+next_number <= 20:
                    dp[k][idx+next_number] += dp[k-1][idx]

print(dp[N-2][arr[-1]])
