# https://www.acmicpc.net/problem/14238

import sys

work_recode = list(input())
A_num, B_num, C_num = (
    work_recode.count("A"),
    work_recode.count("B"),
    work_recode.count("C"),
)

dp = [
    [
        [[[0] * (C_num + 1) for _ in range(B_num + 1)] for _ in range(A_num + 1)]
        for _ in range(3)
    ]
    for _ in range(3)
]


def dfs(A, B, C, string, prev, pprev):
    if A == B == C == 0:
        print(string)
        sys.exit()

    if A > 0 and not dp[0][prev][A - 1][B][C]:
        dfs(A - 1, B, C, string + "A", 0, prev)
        dp[0][prev][A - 1][B][C] = 1

    if B > 0 and prev != 1 and not dp[1][prev][A][B - 1][C]:
        dfs(A, B - 1, C, string + "B", 1, prev)
        dp[1][prev][A][B - 1][C] = 1
    if C > 0 and prev != 2 and pprev != 2 and not dp[2][prev][A][B][C - 1]:

        dfs(A, B, C - 1, string + "C", 2, prev)
        dp[2][prev][A][B][C - 1] = 1


dfs(A_num, B_num, C_num, "", 0, 0)
print(-1)
