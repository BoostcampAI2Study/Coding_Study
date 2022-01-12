import sys
from collections import deque

input = sys.stdin.readline
# L <= 두 나라의 인구차이 <= R이면, 국경선을 연다.
# 위의 조건에 해당하는 국경선이 열리면 인구 이동을 시작한다.
# 인구 이동가능한 나라들 = 연합
# 연합을 이루는 각 칸의 인구수는 연합의 인구수/연합을 이루고 있는 칸의 개수
# 인구이동이 몇일동안 발생하는지

# N = 땅크기, L = 최소인구, R = 최대인구
N, L, R = map(int, input().split())

# 나라 인구수 저장
countries = [list(map(int, input().split())) for _ in range(N)]

# 인구이동 발생하는 누적일수
moving_days = 0

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,1,-1]

# 인구이동 시작
while 1:
    visited = [[False]*N for _ in range(N)]
    moving_list = []
    for x in range(N):
        for y in range(N):
            if visited[x][y] == True:
                continue

            sub_moving_list = []
            # bfs 활용
            q = deque()
            q.append((x, y))
            visited[x][y] = True

            while q:
                nx, ny = q.popleft()

                sub_moving_list.append((nx, ny))

                for k in range(4):
                    nnx = nx + dx[k]
                    nny = ny + dy[k]
                    if nnx < 0 or nnx >= N or nny < 0 or nny >= N:
                        continue
                    if visited[nnx][nny] == True:
                        continue
                    # 연합이 될수있는지 확인
                    if L <= abs(countries[nx][ny] - countries[nnx][nny]) <= R:
                        visited[nnx][nny] = True
                        q.append((nnx, nny))

            # 인구이동 가능한 나라들 append
            if len(sub_moving_list) > 1:
                moving_list.append(sub_moving_list)

    # 인구이동이 발생하는지 여부에 따라 실행
    if moving_list:
        for movings in moving_list:
            # 연합 인구수 구하기
            united_peoples = 0
            for moving in movings:
                a, b = moving
                united_peoples += countries[a][b]

            # 인구 이동 실행
            numbers_of_united = len(movings)

            for moving in movings:
                a, b = moving
                countries[a][b] = united_peoples // numbers_of_united

        moving_days += 1
    else:
        break

print(moving_days)





