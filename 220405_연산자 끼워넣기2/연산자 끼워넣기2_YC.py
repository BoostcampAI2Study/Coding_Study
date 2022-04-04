import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

minim, maxim = float('inf'), -float('inf')

def dfs(result, idx, add, sub, mul, div):
    global minim, maxim
    if idx == N:
        minim = min(minim, result)
        maxim = max(maxim, result)
        return

    if add:
        dfs(result+A[idx], idx+1, add-1, sub, mul, div)
    if sub:
        dfs(result-A[idx], idx+1, add, sub-1, mul, div)
    if mul:
        dfs(result*A[idx], idx+1, add, sub, mul-1, div)
    if div:
        if result < 0:
            dfs(-((-result)//A[idx]), idx+1, add, sub, mul, div-1)
        else:
            dfs(result//A[idx], idx+1, add, sub, mul, div-1)

dfs(A[0], 1, add, sub, mul, div)
print(maxim)
print(minim)
