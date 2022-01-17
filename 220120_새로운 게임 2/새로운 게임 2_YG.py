import sys
from collections import deque, defaultdict

# 체스판의 크기 N, 말의 개수 K
N, K = map(int, input().split())

# 체스판 입력
chess_pan = [list(map(int, input().split())) for _ in range(N)]

# 말 정보 입력
mal_info = [[]]
for _ in range(K):
    x, y, d = map(int, input().split())
    mal_info.append([x-1, y-1, d])

# 방향 설정 1234 = 오른쪽, 왼쪽, 위쪽, 아래쪽
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
direction_reverse = {1:2, 2:1, 3:4, 4:3}

# 좌표별로 말쌓인거 저장
db = defaultdict(list)
for k in range(1, K+1):
    x, y, d = mal_info[k]
    db[x*N+y].append(k)

# 게임시작
for turn in range(1, 1001):
    # 1 ~ k 순으로 게임진행
    for k in range(1, K+1):
        # 종료 여부 확인
        for d in db:
            if len(db[d]) >= 4:
                print(turn)
                sys.exit()

        x, y, d = mal_info[k]
        nx, ny = x+dx[d], y+dy[d]

        if 0 <= nx < N and 0 <= ny < N:
            # 흰색
            if chess_pan[nx][ny] == 0:
                # 이동
                remain = db[x*N+y][:db[x*N+y].index(k)]
                move = db[x*N+y][db[x*N+y].index(k):]
                db[nx*N+ny] += move
                db[x*N+y] = remain
                # 좌표 정보 업데이트
                for mal in move:
                    mal_info[mal][0], mal_info[mal][1] = nx, ny
            # 빨
            elif chess_pan[nx][ny] == 1:
                # 이동
                remain = db[x*N+y][:db[x*N+y].index(k)]
                move = db[x*N+y][db[x*N+y].index(k):][::-1]
                db[nx*N+ny] += move
                db[x*N+y] = remain
                # 좌표 정보 업데이트
                for mal in move:
                    mal_info[mal][0], mal_info[mal][1] = nx, ny
            # 파
            else:
                nx = x - dx[d]
                ny = y - dy[d]

                mal_info[k][2] = direction_reverse[mal_info[k][2]]
                if 0 <= nx < N and 0 <= ny < N:
                    # 흰색
                    if chess_pan[nx][ny] == 0:
                        # 이동
                        remain = db[x*N+y][:db[x*N+y].index(k)]
                        move = db[x*N+y][db[x*N+y].index(k):]
                        db[nx*N+ny] += move
                        db[x*N+y] = remain
                        # 좌표 정보 업데이트
                        for mal in move:
                            mal_info[mal][0], mal_info[mal][1] = nx, ny
                    # 빨
                    elif chess_pan[nx][ny] == 1:
                        # 이동
                        remain = db[x*N+y][:db[x*N+y].index(k)]
                        move = db[x*N+y][db[x*N+y].index(k):][::-1]
                        db[nx*N+ny] += move
                        db[x*N+y] = remain
                        # 좌표 정보 업데이트
                        for mal in move:
                            mal_info[mal][0], mal_info[mal][1] = nx, ny

        # 파란색과 같은 경우
        else:
            nx = x - dx[d]
            ny = y - dy[d]
            mal_info[k][2] = direction_reverse[mal_info[k][2]]
            if 0 <= nx < N and 0 <= ny < N:
                # 흰색
                if chess_pan[nx][ny] == 0:
                    # 이동
                    remain = db[x*N+y][:db[x*N+y].index(k)]
                    move = db[x*N+y][db[x*N+y].index(k):]
                    db[nx*N+ny] += move
                    db[x*N+y] = remain
                    # 좌표 정보 업데이트
                    for mal in move:
                        mal_info[mal][0], mal_info[mal][1] = nx, ny
                # 빨
                elif chess_pan[nx][ny] == 1:
                    # 이동
                    remain = db[x*N+y][:db[x*N+y].index(k)]
                    move = db[x*N+y][db[x*N+y].index(k):][::-1]
                    db[nx*N+ny] += move
                    db[x*N+y] = remain
                    # 좌표 정보 업데이트
                    for mal in move:
                        mal_info[mal][0], mal_info[mal][1] = nx, ny


    # 종료 여부 확인
    for d in db:
        if len(db[d]) >= 4:
            print(turn)
            sys.exit()

print(-1)