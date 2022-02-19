# catalan: https://ko.wikipedia.org/wiki/카탈랑_수
N = int(input())
L_list = [int(input()) for _ in range(N)]

max_L = max(L_list)
dp = [0] * 2501

def catalan(num):
    dp[0] = 1
    for i in range(1, num + 1):
        dp[i] = dp[i - 1] * 2 * (2 * i - 1) // (i + 1)

catalan(int(max_L / 2))
for L in L_list:
    if L % 2 != 0:
        print(0)
    else:
        print(dp[int(L / 2)] % 1000000007)
