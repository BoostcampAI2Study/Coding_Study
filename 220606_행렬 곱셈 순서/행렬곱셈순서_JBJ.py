import sys

N = int(sys.stdin.readline().rstrip())
MATRICES = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

for multi_mat_num in range(1, N):
    for smi in range(N-multi_mat_num): # [S]tart [M]atrix [I]ndex
        emi = smi+multi_mat_num # [E]nd [M]atrix [I]ndex
        if multi_mat_num == 1:
            dp[smi][emi] = MATRICES[smi][0] * MATRICES[smi][1] * MATRICES[emi][1]
        else:
            if dp[smi][emi] == 0: dp[smi][emi] = 2**31
            for imi in range(smi, emi): # [I]ntermediate [M]atrix [I]ndex
                dp[smi][emi] = min(dp[smi][emi],
                    dp[smi][imi] + dp[imi+1][emi] + (MATRICES[smi][0] * MATRICES[imi][1] * MATRICES[emi][1]))
print(dp[0][N-1])
