import sys
sys.setrecursionlimit(10 ** 4)
N = int(input())
board = [-1] * N
result = 0

def dfs(cnt):
    global result
    if cnt == N:
        result += 1
        return
    for c in range(N):
        for r in range(cnt):
            if board[r] == c or abs(cnt - r) == abs(c - board[r]):
                break
        else:
            board[cnt] = c
            dfs(cnt + 1)
dfs(0)
print(result)
