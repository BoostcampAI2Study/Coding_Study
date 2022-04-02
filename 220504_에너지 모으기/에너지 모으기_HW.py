import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
weights = list(map(int, sys.stdin.readline().split()))

check = [False] * N
result = -1
def dfs(energy, cnt):
    global result
    result = max(result, energy)

    for i in range(1, N-1):
        if not check[i]:
            new_energy = 0
            for j in range(i - 1, -1, -1):
                if not check[j]:
                    new_energy += weights[j]
                    break
            for j in range(i + 1, N):
                if not check[j]:
                    new_energy *= weights[j]
                    break
            check[i] = True
            dfs(energy + new_energy, cnt + 1)
            check[i] = False
dfs(0, 0)
print(result)
