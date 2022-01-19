import sys
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def dfs(r, c, value, length):
    
    global answer

    # 테트로미노 길이가 4일경우 return
    if length >= 4:
        answer = max(answer, value)
        return
    
    for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
        nr, nc = r + dr, c + dc

        if nr < 0 or N <= nr or nc < 0 or M <= nc:
            continue
        if visit[nr][nc]:
            continue

        visit[nr][nc] = True
        dfs(nr, nc, value + graph[nr][nc], length+1)
        visit[nr][nc] = False

def T(r, c):
    global answer

    # 시작점 (0,0) 기준 좌표
    shapes = [[(0,0), (1,0), (2,0), (1,1)], # ㅏ 
             [(0,0), (1,0), (2,0), (1,-1)], # ㅓ
             [(0,0), (0,1), (0,2), (-1,1)], # ㅗ
             [(0,0), (0,1), (0,2), (1,1)]]  # ㅜ
    
    for shape in shapes:
        summ = 0
        for dr, dc in shape:
            nr, nc = r+dr, c+dc

            if nr < 0 or N <= nr or nc < 0 or M <= nc:
                continue
            summ += graph[nr][nc]
        answer = max(answer, summ)


visit = [[False] * M for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(M):

        visit[i][j] = True
        dfs(i, j, graph[i][j], 1)
        visit[i][j] = False

        # ㅜ 모양 따로 처리.
        T(i, j)

print(answer)
