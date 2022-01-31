import sys
input = sys.stdin.readline

N, S, M = list(map(int, input().split()))
V = list(map(int, input().split()))

answer = -1
def dfs(m, i, cnt):
    global answer
    if i == len(V):
        answer = max(answer, cnt)
        return
    if cnt + V[i] <= m:
        dfs(m, i+1, cnt+V[i])
    if cnt - V[i] >= 0:
        dfs(m, i+1, cnt-V[i])

dfs(M, 0, S)
print(answer)
