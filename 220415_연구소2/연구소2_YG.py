import sys
from collections import deque
from itertools import combinations
import copy
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

virus_list = []
blank_list = []
wall_list = []
for x in range(N):
    for y in range(N):
        if graph[x][y] == 2:
            virus_list.append((x, y))
        elif graph[x][y] == 0:
            blank_list.append((x, y))
        else:
            wall_list.append((x, y))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

answer = 1e9
for combo in list(combinations(virus_list, M)):
    n_graph = copy.deepcopy(graph)
    count = 0
    # 바이러스 놓기
    for a, b in virus_list:
        for na, nb in combo:
            if a == na and b == nb:
                n_graph[a][b] = 2
            else:
                n_graph[a][b] = 0

    # 바이러스 퍼지기 (BFS)
    q = deque()
    visited = [[False]*N for _ in range(N)]
    for a, b in combo:
        visited[a][b] = True
        q.append((a, b, 0))


    while q:
        nx, ny, time = q.popleft()
        count += 1
        if count + len(wall_list) == N*N:
            answer = min(answer, time)
            break

        for k in range(4):
            nnx, nny = nx+dx[k], ny+dy[k]
            if 0 <= nnx < N and 0 <= nny < N and visited[nnx][nny] == False and n_graph[nnx][nny] == 0:
                n_graph[nnx][nny] = 2
                visited[nnx][nny] = True
                q.append((nnx, nny, time+1))

if answer == 1e9:
    print(-1)
else:
    print(answer)