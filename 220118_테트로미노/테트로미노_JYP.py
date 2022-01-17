import sys

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
v = [[False] * M for _ in range(N)]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = -sys.maxsize

# dist = 4 is criteria
def dfs(r, c, dist, total):
    global ans
    if dist == 4:
        ans = max(ans, total)
        return

    for dir in dirs:
        nx = r + dir[0]
        ny = c + dir[1]

        if 0 <= nx < N and 0 <= ny < M and not v[nx][ny]:
            v[nx][ny] = True
            dfs(nx, ny, dist + 1, total + maps[nx][ny])
            v[nx][ny] = False

def check_fuck_you(r, c):
    global ans
    tmps = []
    for dir in dirs:
        nx = r + dir[0]
        ny = c + dir[1]

        if 0 <= nx < N and 0 <= ny < M:
            tmps.append(maps[nx][ny])

    tmps.sort(reverse=True)
    if len(tmps) >= 3:
        ans = max(ans, maps[r][c] + sum(tmps[:3]))

for i in range(N):
    for j in range(M):
        v[i][j] = True
        dfs(i, j, 1, maps[i][j])
        v[i][j] = False

        # 보큐 별도 처리
        check_fuck_you(i, j)

print(ans)
