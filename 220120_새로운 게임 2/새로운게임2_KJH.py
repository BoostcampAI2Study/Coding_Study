# https://www.acmicpc.net/problem/17837

import sys


N, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

chess_info = [[[] for _ in range(N)] for _ in range(N)]
horses_info = [0] * (K + 1)
for i in range(1, K + 1):
    x, y, direction = map(int, input().split())
    horses_info[i] = [(x - 1, y - 1), direction]  # 좌표, 방향
    chess_info[x - 1][y - 1] = [i]

directions = [None, (0, 1), (0, -1), (-1, 0), (1, 0)]
answer = 1


def update(horse_num, is_blue=False):
    (x, y), direction = horses_info[horse_num]
    dx, dy = directions[direction]
    nx, ny = x + dx, y + dy
    if 0 <= nx < N and 0 <= ny < N:
        floor = chess_info[x][y].index(horse_num)
        if table[nx][ny] == 0:
            chess_info[nx][ny] += chess_info[x][y][floor:]

        elif table[nx][ny] == 1:
            chess_info[nx][ny] += chess_info[x][y][floor:][::-1]

        else:
            if is_blue:
                return nx, ny
            direction += 1 if direction % 2 else -1
            horses_info[i][1] = direction
            return update(horse_num, True)

        # 좌표 업데이트
        if 0 <= nx < N and 0 <= ny < N and table[nx][ny] != 2:
            for j in range(len(chess_info[nx][ny])):
                horses_info[chess_info[nx][ny][j]][0] = (nx, ny)
        chess_info[x][y] = chess_info[x][y][:floor]
    else:
        if is_blue:
            return nx, ny
        direction += 1 if direction % 2 else -1
        horses_info[i][1] = direction
        return update(horse_num, True)
    return nx, ny


for _ in range(1001):
    for i in range(1, K + 1):
        nx, ny = update(i)
        if 0 <= nx < N and 0 <= ny < N and len(chess_info[nx][ny]) >= 4:
            print(answer)
            sys.exit()
    answer += 1
print(-1)
