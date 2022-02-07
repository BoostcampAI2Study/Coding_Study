## 블로그 힌트랑 예시 답안 코드 참고해서 작성했음

import sys
input = sys.stdin.readline

def dfs(r, c, total,size):
    global ans
    if size == 4:
        ans = max(ans, total)
        return

    for mr, mc in moves:
        new_r, new_c = r+mr, c+mc

        if 0<= new_r < N and 0<= new_c < M and not visited[new_r][new_c]:
            
            if size == 2:
                visited[new_r][new_c] = True
                dfs(r, c, total+A[new_r][new_c],size+1)
                visited[new_r][new_c] = False

            visited[new_r][new_c] = True
            dfs(new_r, new_c, total+A[new_r][new_c],size+1)
            visited[new_r][new_c] = False


moves=[[-1,0],[0,1],[1,0],[0,-1]]

N, M = map(int, input().split())
visited=[[False for _ in range(M)] for _ in range(N)]
A=[]
for _ in range(N):
    A.append(list(map(int, input().split())))
ans=0
for r in range(N):
    for c in range(M):
        visited[r][c] = True
        dfs(r,c,A[r][c],1)
        visited[r][c] = False
print(ans)