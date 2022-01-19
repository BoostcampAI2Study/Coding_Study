import sys

def DFS(r,c,depth,sum,visited,board):
    visited[r][c] = True
    sum += board[r][c]
    if depth == 3:
        return sum
    for dir_r, dir_c in (0,1),(0,-1),(1,0),(-1,0):
        togo_r, togo_c=r+dir_r, c+dir_c
        if 0 <= togo_r < N and 0 <= togo_c < N and not visited[togo_r][togo_c]:
            DFS(togo_r,togo_c,depth+1,sum,visited,board)

def Tetrominos(N,M,board, visited):
    max = 0
    for i in range(N):
        for j in range(M):
            total = DFS(i,j,0,0,visited,board)
            if total > max:
                max = total
    



N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

print(Tetrominos(N,M,board, visited))


## 모르겠네용...