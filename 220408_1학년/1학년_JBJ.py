N = int(input().rstrip())
NUMS = list(map(int, input().rstrip().split()))
dp = [[0]*21 for _ in range(N-1)]
dp[0][NUMS[0]] = 1

for num_idx in range(1, N-1):
    num = NUMS[num_idx]
    for sum_idx in range(21):
        if dp[num_idx-1][sum_idx]:
            if 0 <= sum_idx-num <= 20:
                dp[num_idx][sum_idx-num] += dp[num_idx-1][sum_idx]
            if 0 <= sum_idx+num <= 20:
                dp[num_idx][sum_idx+num] += dp[num_idx-1][sum_idx]
                
print(dp[-1][NUMS[-1]])