import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(M)]

room_sizes = [[0]*N for _ in range(M)]
checking_room = [[0]*N for _ in range(M)]
# 남 동 북 서
dx = [1,0,-1,0]
dy = [0,1,0,-1]

answer1, answer2 = 0, 0
visited = [[False]*N for _ in range(M)]
for x in range(M):
    for y in range(N):
        if visited[x][y]:
            continue
        answer1 += 1
        visited[x][y] = True
        q = deque()
        q.append((x, y))
        rooms_idx = []
        rooms_max = 0

        while q:
            nx, ny = q.popleft()

            rooms_idx.append((nx, ny))
            rooms_max += 1

            code = format(graph[nx][ny], 'b')

            code = (4-len(code))*'0'+code

            # 남 동 북 서
            # 조건에 맞다면 보내준다.
            for k in range(4):
                # 벽은 continue
                if int(code[k]) == 1:
                    continue
                nnx, nny = nx+dx[k], ny+dy[k]

                if visited[nnx][nny]:
                    continue
                visited[nnx][nny] = True
                q.append((nnx, nny))

        for a, b in rooms_idx:
            room_sizes[a][b] = rooms_max
            checking_room[a][b] = answer1
        answer2 = max(answer2, rooms_max)

print(answer1)
print(answer2)
# 답 찾아서 출력
answer3 = 0

for x in range(M):
    for y in range(N):
        for k in range(4):
            nx, ny = x + dx[k], y+dy[k]
            if 0 <= nx < M and 0 <= ny < N:
                if checking_room[x][y] == checking_room[nx][ny]:
                    continue
                answer3 = max(answer3, room_sizes[x][y]+room_sizes[nx][ny])
print(answer3)