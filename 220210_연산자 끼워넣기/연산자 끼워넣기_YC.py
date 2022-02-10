def dfs(value, idx, add, sub, mul, div):
    global mx, mn

    if idx == N:
        mx = max(mx,value)
        mn = min(mn,value)
        return

    if add:
        dfs(value+A[idx], idx+1, add-1, sub, mul, div)
    if sub:
        dfs(value-A[idx], idx+1, add, sub-1, mul, div)
    if mul:
        dfs(value*A[idx], idx+1, add, sub, mul-1, div)
    if div:
        dfs(int(value/A[idx]), idx+1, add, sub, mul, div-1)

N = int(input())

A = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

mx = -float('inf')
mn = float('inf')

dfs(A[0], 1, add, sub, mul, div)

print(mx)
print(mn)