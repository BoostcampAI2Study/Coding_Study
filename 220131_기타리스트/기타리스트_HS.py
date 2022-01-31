import sys
input = sys.stdin.readline

N, S, M = list(map(int, input().split()))
V = list(map(int, input().split())) # 곡 리스트

answer = -1
visited = [[0]*(M+1) for _ in range(N+1)]
visited[0][S] = 1
def dfs(m, i, cnt):
    global answer
    if i == len(V):
        answer = max(answer, cnt)
        return
    # 가지치기
    if cnt + V[i] <= m and not visited[i+1][cnt+V[i]]:
        visited[i+1][cnt+V[i]] = 1
        dfs(m, i+1, cnt+V[i])
    if cnt - V[i] >= 0 and not visited[i+1][cnt-V[i]]:
        visited[i+1][cnt-V[i]] = 1
        dfs(m, i+1, cnt-V[i])

dfs(M, 0, S)
print(answer)
