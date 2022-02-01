import sys

input = sys.stdin.readline

N, S = map(int, input().split())

arr = list(map(int, input().split()))

ans = 0
def dfs(level, value, idx):
    global ans

    if value == S:
        ans += 1

    if level == N:
        return

    for p in range(idx+1, N):
        dfs(level+1, value+arr[p], p)


for k in range(N):
    dfs(1, arr[k], k)

print(ans)