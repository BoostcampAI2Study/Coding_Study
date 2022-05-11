N = int(input())
SEQUENCE = list(map(int, input().split()))
REVERSED_SEQUENCE = reversed(SEQUENCE)

dp = [[0]*(N+1) for _ in range(N+1)] # LCS
for rev_seq_idx, rev_seq_num in enumerate(REVERSED_SEQUENCE, start=1): # [2 4 3 2 1]
    for seq_idx, seq_num in enumerate(SEQUENCE, start=1): # [1 2 3 4 2]
        if seq_num == rev_seq_num:
            dp[rev_seq_idx][seq_idx] = dp[rev_seq_idx-1][seq_idx-1] + 1
        else:
            dp[rev_seq_idx][seq_idx] = max(dp[rev_seq_idx-1][seq_idx], dp[rev_seq_idx][seq_idx-1])

print(N - dp[N][N])
