N = int(input())
graph = [list(input()) for _ in range(N)]

# R==G
from collections import deque

def search(g):
    area = 1
    move = [(0,-1), (-1,0), (0,1), (1,0)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            q=deque()
            q.append((i, j))
            
            if visited[i][j]:
                continue

            while q:
                r, c = q.popleft()

                for dr, dc in move:
                    nr, nc = r+dr, c+dc

                    if 0<=nr<N and 0<=nc<N:
                        if visited[nr][nc]:
                            continue
                        if g[r][c] == g[nr][nc]:
                            visited[nr][nc] = area
                            q.append((nr, nc))
            area += 1
                        
    # print(visited)
    return area-1

graph2 = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph2[i][j] = 'G'
        else:
            graph2[i][j] = graph[i][j]

print(f'{search(graph)} {search(graph2)}')
