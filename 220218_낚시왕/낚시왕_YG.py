import sys
import copy
from collections import defaultdict

input = sys.stdin.readline

#  R, C = 격자판 크기, M = 상어의 수
R, C, M = map(int, input().split())

if M==0:
    print(0)
    sys.exit()

# 상어 정보
db = defaultdict(list)

dx = [0, -1,1,0,0]
dy = [0, 0,0,1,-1]
change_direction = {1:2, 2:1, 3:4, 4:3}

for shark in range(M):
    r, c, s, d, z = map(int, input().split())

    # r, c = 위치, s = 속력, d = 이동 방향, z = 크기
    # d = 1(위), 2(아래), 3(오른쪽), 4(왼쪽)

    if d == 1 or d == 2:
        s %= 2*R-2
    else:
        s %= 2*C-2


    db[shark] = [r-1, c-1, s, d, z]


answer = 0

# 열만큼 낚시
for idx in range(C):
    # 땅과 제일 가까운 상어를 잡음
    distance = 1e9
    catched_fish = -1
    for shark in db:
        if db[shark][1] == idx:
            if db[shark][0] < distance:
                distance = db[shark][0]
                catched_fish = shark

    # 해당 열에 상어가 있다면 잡기
    if catched_fish != -1:
        answer += db[catched_fish][4]
        del(db[catched_fish])

    dup_checked = [[[] for _ in range(C)] for _ in range(R)]

    dup_list = []
    # 상어 이동
    for shark in db:
        # r, c = 위치, s = 속력, d = 이동 방향, z = 크기
        nr, nc, ns, nd, nz = db[shark]

        move = 0
        while 1:
            if move == ns:
                break

            nnr, nnc = nr + dx[nd], nc + dy[nd]

            if 0 <= nnr < R and 0 <= nnc < C:
                nr, nc = nnr, nnc
                move += 1
            else:
                nd = change_direction[nd]

        db[shark] = [nr, nc, ns, nd, nz]

        if not dup_checked[nr][nc]:
            dup_checked[nr][nc] = [nz,shark]
        else:
            if nz > dup_checked[nr][nc][0]:
                dup_list.append(dup_checked[nr][nc][1])
                dup_checked[nr][nc] = [nz, shark]
            else:
                dup_list.append(shark)

    # 겹친다면 가장 큰 상어만 남기기
    for dup in dup_list:
        del db[dup]

print(answer)