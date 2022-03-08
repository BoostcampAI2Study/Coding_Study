import sys
N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
questions = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

dp = [[-1] * len(sequence) for _ in range(len(sequence))]
def palindrome(start, end):
    if dp[start][end] != -1:
        return dp[start][end]
    if start == end:
        dp[start][end] = 1
        return 1
    if sequence[start] == sequence[end]:
        if start + 1 == end:
            dp[start][end] = 1
        else:
            dp[start][end] = palindrome(start + 1, end - 1)
    else:
        dp[start][end] = 0
    return dp[start][end]

for i in range(M):
    print(1) if palindrome(questions[i][0] - 1, questions[i][1] - 1) else print(0)
