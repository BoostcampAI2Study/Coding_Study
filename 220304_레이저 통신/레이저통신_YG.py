import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

W, H = map(int, input().split())

target = []

graph = []
for x in range(H):
    sub = list(input())
    graph.append(sub)

for x in range(H):
    for y in range(W):
        if graph[x][y] == 'C':
            target.append((x, y))


tx, ty = target[1][0], target[1][1]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = []

# 거울개수, x, y, 가던 방향
heapq.heappush(q, (0, target[0][0], target[0][1], -1))
distance = [[INF]*W for _ in range(H)]

distance[target[0][0]][target[0][1]] = 0

while q:
    guwol, x, y, direct = heapq.heappop(q)

    if x == tx and y == ty:
        print(guwol)
        sys.exit()

    if distance[x][y] < guwol:
        continue

    distance[x][y] = guwol

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] != '*':

            if direct == -1 or direct == k:
                heapq.heappush(q, (guwol, nx, ny, k))
            else:
                heapq.heappush(q, (guwol+1, nx, ny, k))
