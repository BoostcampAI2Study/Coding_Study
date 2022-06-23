import sys
def dfs(a_cnt, b_cnt, c_cnt, prev, pprev, sequence):
    if len(sequence) == len(S):
        print(sequence)
        sys.exit()
        return
    if a_cnt > 0 and not dp[0][prev][a_cnt - 1][b_cnt][c_cnt]:
        dfs(a_cnt - 1, b_cnt, c_cnt, 0, prev, sequence + "A")
        dp[0][prev][a_cnt - 1][b_cnt][c_cnt] = True
    if b_cnt > 0 and prev != 1 and not dp[1][prev][a_cnt][b_cnt - 1][c_cnt]:
        dfs(a_cnt, b_cnt - 1, c_cnt, 1, prev, sequence + "B")
        dp[1][prev][a_cnt][b_cnt - 1][c_cnt] = True
    if c_cnt > 0 and prev != 2 and pprev != 2 and not dp[2][prev][a_cnt][b_cnt][c_cnt - 1]:
        dfs(a_cnt, b_cnt, c_cnt - 1, 2, prev, sequence + "C")
        dp[2][prev][a_cnt][b_cnt][c_cnt - 1] = True

S = sys.stdin.readline().strip()
dp = [[[[[False] * 51 for _ in range(51)] for _ in range(51)] for _ in range(3)] for _ in range(3)]
dfs(S.count('A'), S.count('B'), S.count('C'), 0, 0, '')
print(-1)
