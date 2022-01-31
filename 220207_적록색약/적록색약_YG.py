from collections import deque
import sys
import copy

input = sys.stdin.readline

N = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

graph = [list(input()) for _ in range(N)]

# BFS 1
visited_1 = [[False]*N for _ in range(N)]

q1 = deque()
ans_1 = 0
for x in range(N):
    for y in range(N):
        if visited_1[x][y] == False:
            ans_1 += 1
            q1.append((x, y))
            visited_1[x][y] = True
            color_1 = graph[x][y]
            while q1:
                nx, ny = q1.popleft()

                for k in range(4):
                    nnx, nny = nx+dx[k], ny+dy[k]
                    if 0 <= nnx < N and 0 <= nny < N and visited_1[nnx][nny] == False and graph[nnx][nny] == color_1:
                        q1.append((nnx, nny))
                        visited_1[nnx][nny] = True


# BFS 2
visited_2 = [[False]*N for _ in range(N)]
graph_2 = copy.deepcopy(graph)

for x in range(N):
    for y in range(N):
        if graph_2[x][y] == 'R':
            graph_2[x][y] = 'G'

q2 = deque()
ans_2 = 0
for x in range(N):
    for y in range(N):
        if visited_2[x][y] == False:
            ans_2 += 1
            q2.append((x, y))
            visited_2[x][y] = True
            color_2 = graph_2[x][y]
            while q2:
                nx, ny = q2.popleft()

                for k in range(4):
                    nnx, nny = nx+dx[k], ny+dy[k]
                    if 0 <= nnx < N and 0 <= nny < N and visited_2[nnx][nny] == False and graph_2[nnx][nny] == color_2:
                        q2.append((nnx, nny))
                        visited_2[nnx][nny] = True

print(ans_1, ans_2)