# https://www.acmicpc.net/problem/2234

"""
출력
    이 성에 있는 방의 개수
    가장 넓은 방의 넓이
    하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

direction_map = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}


def movable_direction(binary):
    directions = []
    binary = "0" * (4 - len(bin(binary)[2:])) + bin(binary)[2:]
    for idx, b in enumerate(binary):
        if b == "0":
            directions.append(direction_map[idx])
    return directions


blocks = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]


def dfs(node, room):
    global cnt
    x, y = node
    if visited[x][y]:
        return
    visited[x][y] = room
    cnt += 1
    for dx, dy in movable_direction(blocks[x][y]):
        nx, ny = x + dx, y + dy
        if visited[nx][ny]:
            continue
        dfs((nx, ny), room)


room_num = 1
room_size = {}
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            cnt = 0
            dfs((i, j), room_num)
            room_size[room_num] = cnt
            room_num += 1

answer1 = len(room_size)
answer2 = max(room_size.values())

checked = [[0] * N for _ in range(M)]


def check_surround(node):
    global surround
    x, y = node
    if checked[x][y]:
        return
    checked[x][y] = 1
    for dx, dy in direction_map.values():
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N:
            if not checked[nx][ny]:
                if visited[nx][ny] == visited[x][y]:
                    check_surround((nx, ny))
                else:
                    surround.add(visited[nx][ny])


for i in range(M):
    for j in range(N):
        if not checked[i][j]:
            surround = set()
            check_surround((i, j))
            for room in surround:
                answer3 = max(answer3, room_size[visited[i][j]] + room_size[room])

print(answer1)
print(answer2)
print(answer3)
