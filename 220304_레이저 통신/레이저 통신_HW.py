import collections
W, H = map(int, input().split())
maps = [input() for _ in range(H)]

NR = [0, 0, 1, -1]
NC = [1, -1, 0, 0]
visited = [[1e9] * W for _ in range(H)]
reverse_direct = {0:1, 1:0, 2:3, 3:2}
min_result = 1e9

# C 위치 찾기
squares = []
for r in range(H):
    for c in range(W):
        if maps[r][c] == 'C':
            squares.append((r, c))

# 첫번째 C에서 동서남북 탐색
q = collections.deque()
visited[squares[0][0]][squares[0][1]] = 0
min_mirror = 1e9
for i in range(4):
    nr, nc = squares[0][0] + NR[i], squares[0][1] + NC[i]
    if 0 <= nr < H and 0 <= nc < W and maps[nr][nc] == '.':
        q.append((nr, nc, i, 0))
        visited[nr][nc] = 0
        
while q:
    r, c, direct, mirror = q.popleft()
    if mirror != visited[r][c]:
        continue
    if r == squares[1][0] and c == squares[1][1] and min_result > mirror:
        min_result = mirror
        continue
    for i in range(4):
        nr, nc = r + NR[i], c + NC[i]
        if 0 <= nr < H and 0 <= nc < W:
            if maps[nr][nc] != '*':
                next_mirror = mirror
                if i == reverse_direct[i]:
                    continue
                if i != direct:
                    next_mirror += 1
                if visited[nr][nc] >= next_mirror:
                    q.append((nr, nc, i, next_mirror))
                    visited[nr][nc] = next_mirror
print(min_result)
