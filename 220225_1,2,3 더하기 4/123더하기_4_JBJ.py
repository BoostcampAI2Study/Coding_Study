import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    if N > 3:
        dp = [[0]*(N+1) for _ in range(4)] # (end number, sum) e.g. dp[3][3] = 1, # of summations that end with '3' = 1
        # (1: 1), (2: 1+1), (2: 2), (3: 1+1+1), (3: 1+2), (3: 3)
        dp[1][1], dp[1][2], dp[2][2], dp[1][3], dp[2][3], dp[3][3] = 1, 1, 1, 1, 1, 1

        for cur_sum in range(4, N+1): # summations in ascending order - avoid duplications
            dp[1][cur_sum] = dp[1][cur_sum-1]
            dp[2][cur_sum] = dp[1][cur_sum-2] + dp[2][cur_sum-2] 
            dp[3][cur_sum] = dp[1][cur_sum-3] + dp[2][cur_sum-3] + dp[3][cur_sum-3]

        print(dp[1][N] + dp[2][N] + dp[3][N])
    else:
        print(N)