import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

color_blind={'R':['R','G'],'G':['R','G'],'B':['B']}

moves = [[0,1],[1,0],[0,-1],[-1,0]]

def dfs(r,c,color,blind=False):
    if blind:
        for mr, mc in moves:
            nr,nc = r+mr, c+mc
            if 0<=nr<N and 0<=nc<N:
                if not visited[nr][nc] and picture[nr][nc] in color_blind[color]:
                    visited[nr][nc] = color
                    dfs(nr, nc, color, blind)
    else:
        for mr, mc in moves:
            nr,nc = r+mr, c+mc
            if 0<=nr<N and 0<=nc<N:
                if not visited[nr][nc] and picture[nr][nc] == color:
                    visited[nr][nc] = color
                    dfs(nr, nc, color, blind)

N = int(input())
picture = [list(input()) for _ in range(N)]

answer=[]
for blind in range(2):
    colors = {'R':0,'B':0,'G':0}
    visited=[[False for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                colors[picture[r][c]]+=1
                dfs(r,c,picture[r][c], blind)

    answer.append(sum(colors.values()))

for a in answer: print(a,end=' ')