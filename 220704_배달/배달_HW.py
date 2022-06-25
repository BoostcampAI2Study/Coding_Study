import sys, collections

N, M = map(int, sys.stdin.readline().split())
MAP = [sys.stdin.readline().strip() for _ in range(N)]

# find locations
cur_loc, presents = [], []
for r in range(N):
    for c in range(M):
        if MAP[r][c] == 'S':
            cur_loc = [r, c]
        elif MAP[r][c] == 'C':
            presents.append([r, c])

NR, NC = [0, 0, 1, -1], [1, -1, 0, 0]
q = collections.deque()
q.append((cur_loc[0], cur_loc[1], -1, 0, False, False))
visit = [[[[False] * 3 for _ in range(4)] for _ in range(M)] for _ in range(N)]
result = -1
while q:
    r, c, d, t, p1, p2 = q.popleft()
    if r == presents[0][0] and c == presents[0][1]:
        p1 = True
    if r == presents[1][0] and c == presents[1][1]:
        p2 = True
    if p1 and p2:
        result = t
        break

    presents_visit = 0
    if p1:
        presents_visit = 1
    elif p2:
        presents_visit = 2

    for i in range(4):
        if i == d:
            continue
        nr, nc = r + NR[i], c + NC[i]
        if 0 <= nr < N and 0 <= nc < M and MAP[nr][nc] != '#' and not visit[nr][nc][i][presents_visit]:
            q.append((nr, nc, i, t + 1, p1, p2))
            visit[nr][nc][i][presents_visit] = True

print(result)
