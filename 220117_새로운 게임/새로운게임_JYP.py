n, k = map(int, input().split())
chess = [list(map(int, input().split())) for _ in range(n)]
horses = [-1 for _ in range(k)]
maps = [[[] for _ in range(n)] for _ in range(n)]

for i in range(k):
    r, c, d = map(int, input().split())
    maps[r - 1][c - 1].append(i)
    horses[i] = [r - 1, c - 1, d]

dirs = {
    1: (0, 1),
    2: (0, -1),
    3: (-1, 0),
    4: (1, 0)
}

ch_dirs = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}

cnt = 1
while cnt <= 1000:
    for i in range(k):
        # current horse
        cur_r, cur_c, cur_d = horses[i]
        if i != maps[cur_r][cur_c][0]:
            continue

        nx = cur_r + dirs[cur_d][0]
        ny = cur_c + dirs[cur_d][1]

        # blue or out of range
        if nx < 0 or ny < 0 or nx >= n or ny >= n or chess[nx][ny] == 2:
            cur_d = ch_dirs[cur_d]
            horses[i][2] = cur_d

            nx = cur_r + dirs[cur_d][0]
            ny = cur_c + dirs[cur_d][1]

            if nx < 0 or ny < 0 or nx >= n or ny >= n or chess[nx][ny] == 2:
                continue

        tmp_maps = maps[cur_r][cur_c].copy()

        # red
        if chess[nx][ny] == 1:
            tmp_maps = tmp_maps[::-1]

        # relocation
        for j in tmp_maps:
            horses[j][0] = nx
            horses[j][1] = ny
            maps[nx][ny].append(j)

        maps[cur_r][cur_c] = []
        if len(maps[nx][ny]) >= 4:
            print(cnt)
            exit()

    cnt += 1

print(-1)
