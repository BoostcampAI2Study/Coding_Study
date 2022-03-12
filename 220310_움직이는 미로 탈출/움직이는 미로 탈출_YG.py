import sys
from collections import deque

input = sys.stdin.readline

sx, sy = 7, 0
ex, ey = 0, 7

dx = [0,0,0,1,1,1,-1,-1,-1]
dy = [0,1,-1,0,1,-1,0,1,-1]

graph = []
for _ in range(8):
    sub = list(input())
    graph.append(sub)
q = deque()

q.append((sx, sy))

cnt = 1
while q:
    sub_q = []
    for _ in range(cnt):
        x, y = q.popleft()
        # 9방향으로 움직이기

        for k in range(9):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < 8 and 0 <= ny < 8 and graph[nx][ny] == '.':
                sub_q.append((nx, ny))

    # 벽 이동하기
    graph = [['.']*8] + graph[:-1]

    cnt = 0
    # 벽 이동 후 안만나면 q에 넣기
    for a, b in sub_q:
        if graph[a][b] != '#':
            if a == ex and b == ey:
                print(1)
                sys.exit()
            q.append((a, b))
            cnt += 1

print(0)