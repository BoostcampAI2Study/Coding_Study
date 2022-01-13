import sys
from collections import deque, defaultdict

input = sys.stdin.readline
# N x N 체스판, 말의 개수는 K개
# 하나의 말 위에 다른 말을 올릴 수 있다.
# 각 칸은 흰색(0), 빨간색(1), 파란색(2) 중 하나로 색칠되어 있다.
# 체스판에 말 K개 놓고 게임 시작 (말은 1~K번 번호가 매겨져 있고, 이동 방향도 미리 정해져 있다.)
# 이동 방향은 상하좌우

# 턴 한번은 1번에서 K번말까지 순서대로 이동 (올려져 있는 말도 함께 이동, 가장 아래의 말만 이동가능)
# 말이 4개쌓이면 게임 종료
# direction 1 = 오른쪽, 2 = 왼쪽, 3 = 위쪽, 4 = 아래쪽
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
direction_turn = {1:2, 2:1, 3:4, 4:3}

# N = 크기, K = 말의 개수
N, K = map(int, input().split())

# 체스판 정보
arr = [list(map(int, input().split())) for _ in range(N)]

# 좌표별 말순서 저장
db = defaultdict(list)

# 체스말 정보
info = [[]]
for idx in range(1, K+1):
    x, y, direction = map(int, input().split())
    info.append([x-1, y-1, direction])
    db[(x-1)*N+(y-1)].append(idx)

# 1000번 넘어가면 -1 출력 & 안넘어가면 그때의 turn 출력
for turn in range(1, 1001):
    # 체스말 순서대로 게임진행
    for pick in range(1, K+1):
        x, y, direction = info[pick]
        # 말중에 가장 아래에 있는 말만 이동
        if db[x*N+y][0] == pick:
            nx, ny = x+dx[direction], y+dy[direction]

            if 0 <= nx < N and 0 <= ny < N:
                # 흰칸인 경우
                if arr[nx][ny] == 0:
                    for picked in db[x*N+y]:
                        info[picked][0] = nx
                        info[picked][1] = ny
                    db[nx*N+ny] += db[x*N+y]
                    db[x*N+y] = []
                # 빨간색인 경우
                elif arr[nx][ny] == 1:
                    for picked in db[x*N+y]:
                        info[picked][0] = nx
                        info[picked][1] = ny
                    db[nx*N+ny] += db[x*N+y][::-1]
                    db[x*N+y] = []
                # 파란색인 경우
                else:
                    nx, ny = nx-dx[direction], ny-dy[direction]
                    nx, ny = nx+dx[direction_turn[direction]], ny+dy[direction_turn[direction]]
                    info[pick] = [x, y, direction_turn[direction]]
                    if 0 <= nx < N and 0 <= ny < N:
                        # 흰칸인 경우
                        if arr[nx][ny] == 0:
                            for picked in db[x*N+y]:
                                info[picked][0] = nx
                                info[picked][1] = ny
                            db[nx*N+ny] += db[x*N+y]
                            db[x*N+y] = []
                        # 빨간색인 경우
                        elif arr[nx][ny] == 1:
                            for picked in db[x*N+y]:
                                info[picked][0] = nx
                                info[picked][1] = ny
                            db[nx*N+ny] += db[x*N+y][::-1]
                            db[x*N+y] = []

            # 벗어나는 경우도 파란색으로 취급
            else:
                nx, ny = nx-dx[direction], ny-dy[direction]
                nx, ny = nx+dx[direction_turn[direction]], ny+dy[direction_turn[direction]]
                info[pick] = [x, y, direction_turn[direction]]
                if 0 <= nx < N and 0 <= ny < N:
                    # 흰칸인 경우
                    if arr[nx][ny] == 0:
                        for picked in db[x*N+y]:
                            info[picked][0] = nx
                            info[picked][1] = ny
                        db[nx*N+ny] += db[x*N+y]
                        db[x*N+y] = []
                    # 빨간색인 경우
                    elif arr[nx][ny] == 1:
                        for picked in db[x*N+y]:
                            info[picked][0] = nx
                            info[picked][1] = ny
                        db[nx*N+ny] += db[x*N+y][::-1]
                        db[x*N+y] = []

        max_chess = 0

        for where in db:
            max_chess = max(max_chess, len(db[where]))

        if max_chess >= 4:
            print(turn)
            sys.exit()

else:
    print(-1)








