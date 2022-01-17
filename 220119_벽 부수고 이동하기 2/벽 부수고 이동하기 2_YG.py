from collections import deque

# 세로 N, 가로 M, 부수기 횟수 K
N, M, K = map(int, input().split())

# 맵 입력받기
arr = [list(map(int, input())) for _ in range(N)]

# 거리정보저장
distances = [[[]] * M for _ in range(N)]
for a in range(N):
    for b in range(M):
        distances[a][b] = [1e9]*(K+1)

# 초기화
distances[0][0][0] = 1

# 이동
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# bfs를 활용하여 거리 계산및 업데이트
q = deque()

# x, y, 벽부순 횟수
q.append((0, 0, 0))

# bfs 진행
while q:
    x, y, count = q.popleft()
    for p in range(4):
        nx = x + dx[p]
        ny = y + dy[p]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0 and distances[nx][ny][count] == 1e9:
                distances[nx][ny][count] = distances[x][y][count]+1
                q.append((nx, ny, count))
            elif arr[nx][ny] == 1 and count+1 <= K and distances[nx][ny][count+1] == 1e9:
                distances[nx][ny][count+1] = distances[x][y][count]+1
                q.append((nx, ny, count+1))

# 답 구하고 출력
answer = min(distances[N-1][M-1])
if answer == 1e9:
    print(-1)
else:
    print(answer)

