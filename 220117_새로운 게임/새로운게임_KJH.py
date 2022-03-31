# https://www.acmicpc.net/problem/17780

"""
이동하려는 칸의 색에 따라 다르게 행동한다
흰색
    단순 이동 , 이동하려는 말에 쌓여있는 모든 말들 함께 이동
빨간색
    이동 후 이동한 말과 그 위의 모든 말 순서를 반대로 바꾼다.
파란색 & 체스판 밖으로 나가려는 경우 
    A번 말의 이동 방향을 반대로 하고 한 칸 이동
    만약 또 다시 같은 조건이 될 경우 이동하지 않고 방향만 반대로
"""

# 빨간색의 경우 가장 아래와 윗 부분만 체크하자

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

color = []
houses = {}  # 해당 말의 방향은 어디인지, 현재 가장 위에 있는 말과 방향은 무엇인지? # dir, [num, dir]
table = [[0] * N for _ in range(N)]  # 테이블이 가지고 있어야하는 정보 몇번 말이 있는지?
for _ in range(N):
    color.append(list(map(int, input().split())))  # 0 :흰, 1:빨, 2:파
for i in range(K):
    c, r, dir = map(int, input().split())
    houses[i + 1] = [
        c - 1,
        r - 1,
        dir,
        1,
        [i + 1, dir],
    ]  # col, row, dir, stack_num, [num, dir]
    table[c - 1][r - 1] = i + 1

direction_mapping = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}

answer = 1


def update(house_num, isblue=False):
    x, y, dir, stack_num, (top_num, top_dir) = houses[house_num]
    dx, dy = direction_mapping[dir]
    if house_num == top_num:
        top_dir = dir
    if 0 <= x + dx < N and 0 <= y + dy < N:
        if color[x + dx][y + dy] == 0:
            if table[x + dx][y + dy]:
                houses[table[x + dx][y + dy]][3] += stack_num
                houses[table[x + dx][y + dy]][4] = [top_num, top_dir]
                houses.pop(house_num)
            else:
                table[x + dx][y + dy] = house_num
                houses[house_num][0] += dx
                houses[house_num][1] += dy
            table[x][y] = 0
        elif color[x + dx][y + dy] == 1:
            houses.pop(house_num)
            houses[top_num] = [x + dx, y + dy, top_dir, stack_num, [house_num, dir]]
            if table[x + dx][y + dy]:
                houses[table[x + dx][y + dy]][3] += stack_num
                houses[table[x + dx][y + dy]][4] = [house_num, dir]
                houses.pop(top_num)
            else:
                table[x + dx][y + dy] = top_num
            table[x][y] = 0

        else:
            if isblue:
                return
            if dir % 2:
                houses[house_num][2] += 1
            else:
                houses[house_num][2] -= 1
            update(house_num, True)

    else:
        if isblue:
            return
        if dir % 2:
            houses[house_num][2] += 1
        else:
            houses[house_num][2] -= 1
        update(house_num, True)


def solution():
    answer = 1
    for _ in range(1001):
        for i in range(1, K + 1):
            if i in houses:
                update(i)
                for _, _, _, stack_num, _ in houses.values():
                    if stack_num >= 4:
                        return answer
        answer += 1
    return -1


print(solution())
