import sys
from collections import deque

N, M, K = map(int, input().split())
maps = [[int(s) for s in sys.stdin.readline().strip()] for _ in range(N)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
v = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]

def bfs():
    # (r, c, cnt)
    q = deque([(0, 0, 0)])
    v[0][0][0] = 1
    while q:
        r, c, cnt = q.popleft()

        # arrival
        if r == N - 1 and c == M - 1:
            return v[r][c][cnt]

        for dir in dirs:
            nx = r + dir[0]
            ny = c + dir[1]

            if 0 <= nx < N and 0 <= ny < M and not v[nx][ny][cnt]:
                # if not movable, check cnt
                if maps[nx][ny] and cnt < K:
                    v[nx][ny][cnt + 1] = v[r][c][cnt] + 1
                    q.append((nx, ny, cnt + 1))
                    continue

                # movable
                if not maps[nx][ny]:
                    v[nx][ny][cnt] = v[r][c][cnt] + 1
                    q.append((nx, ny, cnt))
    return -1

print(bfs())

# 6 4 1
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000
