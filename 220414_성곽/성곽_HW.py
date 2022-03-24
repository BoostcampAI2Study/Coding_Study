import sys, collections
N, M = map(int, sys.stdin.readline().strip().split())
MAPS = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]

visited = [[0] * N for _ in range(M)]
room_cnt, max_room_size, rooms_size = 0, 0, []

NR = [0, -1, 0, 1]
NC = [-1, 0, 1, 0]

def bfs(r, c, room_num):
    q = collections.deque()
    q.append((r, c))
    size = 0
    while q:
        cur_r, cur_c = q.popleft()
        size += 1
        for i in range(4):
            nr, nc = cur_r + NR[i], cur_c + NC[i]
            if not (MAPS[cur_r][cur_c] & (1 << i)) and 0 <= nr < M and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = room_num
                q.append((nr, nc))
    return size

for r in range(M):
    for c in range(N):
        if not visited[r][c]:
            room_cnt += 1
            visited[r][c] = room_cnt
            rooms_size.append(bfs(r, c, room_cnt))

for r in range(M):
    for c in range(N):
        for i in range(4):
            nr, nc = r + NR[i], c + NC[i]
            if MAPS[r][c] & (1 << i) and 0 <= nr < M and 0 <= nc < N and visited[nr][nc] != visited[r][c]:
                max_room_size = max(max_room_size, rooms_size[visited[nr][nc] - 1] + rooms_size[visited[r][c] - 1])

print(room_cnt)
print(max(rooms_size))
print(max_room_size)
