import sys
from collections import defaultdict
from copy import deepcopy
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

graph = []

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

# 물고기 번호 & 방향
for _ in range(4):
    a1, a2, b1, b2, c1, c2, d1, d2 = map(int, input().split())
    graph.append([[a1, a2-1], [b1, b2-1], [c1, c2-1], [d1, d2-1]])

def dfs(shark_x, shark_y, sum_fish, graph):
    global answer

    graph[shark_x][shark_y][0] = 0
    answer = max(answer, sum(sum_fish))

    # 물고기 이동 (1번부터 이동)
    for k in range(1, 17):
        if k in sum_fish:
            continue

        fish_direction = -1
        fish_x, fish_y = -1, -1
        for a in range(4):
            for b in range(4):
                if graph[a][b][0] == k:
                    fish_x, fish_y = a, b
                    fish_direction = graph[a][b][1]
                    break

        for _ in range(8):
            fish_nx, fish_ny = fish_x+dx[fish_direction], fish_y+dy[fish_direction]
            if 0 <= fish_nx < 4 and 0 <= fish_ny < 4:
                if fish_nx == shark_x and fish_ny == shark_y:
                    pass
                else:
                    graph[fish_x][fish_y][1] = fish_direction
                    graph[fish_nx][fish_ny],  graph[fish_x][fish_y] = graph[fish_x][fish_y],  graph[fish_nx][fish_ny]
                    break
            fish_direction += 1
            fish_direction %= 8


    # 상어 먹방 ㄱㄱ
    shark_direction = graph[shark_x][shark_y][1]
    for i in range(1, 5):
        shark_nx, shark_ny = shark_x + dx[shark_direction]*i, shark_y + dy[shark_direction]*i
        if 0 <= shark_nx < 4 and 0 <= shark_ny < 4 and graph[shark_nx][shark_ny][0] != 0:
            eating_fish = graph[shark_nx][shark_ny][0]
            dfs(shark_nx, shark_ny, sum_fish+[eating_fish], deepcopy(graph))


answer = 0
eat = graph[0][0][0]

dfs(0,0,[eat], graph)
print(answer)