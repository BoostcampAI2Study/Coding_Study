T = int(input())
dp = [1, 0, 1] + [0]*4998 # odds: 0, evens: [0: "", 2: "()", ...]

for i in range(4, 5001, 2):
    for j in range(0, i, 2): # DP: (left PS #)(right PS #) cases
        dp[i] += (dp[j] * dp[i-2-j])
        dp[i] %= 1000000007

for _ in range(T):
    n = int(input())
    print(dp[n])