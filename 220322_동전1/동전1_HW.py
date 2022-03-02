# 2차원 배열 메모리 초과 → 1차원 배열로 변경
N, K = map(int, input().split())
coin_values = [int(input()) for _ in range(N)]

dp = [0] * (K + 1)
for n in range(N):
    for k in range(coin_values[n], K + 1):
        if coin_values[n] == k:
            dp[k] += 1
        else:
            dp[k] += dp[k - coin_values[n]]
print(dp[K])

# 2차원 배열
# N, K = map(int, input().split())
# coin_values = [int(input()) for _ in range(N)]
#
# dp = [[0] * (K + 1) for _ in range(N + 1)]
# for n in range(N):
#     for k in range(1, K + 1):
#         if coin_values[n] == k:
#             dp[n + 1][k] = dp[n][k] + dp[n + 1][k - coin_values[n]] + 1
#         elif coin_values[n] > k:
#             dp[n + 1][k] = dp[n][k]
#         else:
#             dp[n + 1][k] = dp[n][k] + dp[n + 1][k - coin_values[n]]
# print(dp[N][K])
