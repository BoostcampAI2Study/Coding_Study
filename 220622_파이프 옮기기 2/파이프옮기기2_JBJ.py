N = int(input())
HOUSE = [input().split() for _ in range(N)]
dp = [[[0]*N for _ in range(N)] for _ in range(3)] # 0: row-wise, 1: coluamn-wise, 2: diagonal-wise

for x in range(1, N):
    if HOUSE[0][x] == '1': break
    dp[0][0][x] = 1

for y in range(1, N):
    for x in range(2, N):
        if HOUSE[y][x] == '1': continue

        dp[0][y][x] = dp[0][y][x-1] + dp[2][y][x-1] # row-wise move case cnt
        dp[1][y][x] = dp[1][y-1][x] + dp[2][y-1][x] # column-wise move case cnt

        if HOUSE[y][x-1] == '1' or HOUSE[y-1][x] == '1': continue
        dp[2][y][x] = dp[0][y-1][x-1] + dp[1][y-1][x-1] + dp[2][y-1][x-1] # diagonal-wise move case cnt

print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])