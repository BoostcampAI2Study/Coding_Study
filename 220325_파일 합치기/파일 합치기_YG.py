# ref: https://data-make.tistory.com/402
# 이런 dp 코테에 안나옴 ㅅㄱ
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # Input
    K = int(input())

    files = list(map(int, input().split()))

    # 누적합
    pre_sum = [0]*(K+1)
    for idx, f in enumerate(files):
        pre_sum[idx+1] += pre_sum[idx]+f

    dp = [[0]*(K+1) for _ in range(K+1)]

    # DP[i][j] : i에서 j까지 합하는데 필요한 최소 비용
    # DP[i][j] = min(DP[i][k] + DP[k+1][j]) + sum(A[i]~A[j])
    for i in range(2, K+1): # 부분 파일의 길이
        for j in range(1, K+2-i):   # 시작점
            dp[j][j+i-1] = min([dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)]) + (pre_sum[j+i-1] - pre_sum[j-1])

    print(dp[1][K])