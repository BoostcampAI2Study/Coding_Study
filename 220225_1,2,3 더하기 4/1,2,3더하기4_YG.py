import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    dp = [[0,0,0,0] for _ in range(10001)]

    dp[1][1] = 1
    dp[2][1] = 1
    dp[2][2] = 1
    dp[3][1] = 1
    dp[3][2] = 1
    dp[3][3] = 1

    if n <= 3:
        print(sum(dp[n]))
    else:
        for idx in range(4, n+1):
            for value in [1,2,3]:
                for idx2, value2 in enumerate(dp[idx-value]):
                    if idx2 <= value:
                        dp[idx][value] += value2

        print(sum(dp[n]))