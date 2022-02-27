R, C, T = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(R)]

NR = [0, 0, 1, -1]
NC = [1, -1, 0, 0]
cleaner = []
# 공기 청정기 위치 확인
for r in range(R):
    if house[r][0] == -1:
        cleaner.append(r)

for t in range(T):
    new_house = [[0] * C for _ in range(R)]
    # 먼지 확산
    for r in range(R):
        for c in range(C):
            if house[r][c] == -1 or house[r][c] == 0:
                new_house[r][c] += house[r][c]
                continue
            dust = house[r][c] // 5
            if dust == 0:
                new_house[r][c] += house[r][c]
                continue
            cnt = 0
            for i in range(4):
                nr, nc = r + NR[i], c + NC[i]
                if 0 <= nr < R and 0 <= nc < C and house[nr][nc] != -1:
                    new_house[nr][nc] += dust
                    cnt += 1
            new_house[r][c] += (house[r][c] - dust * cnt)

    house = new_house
    # 공기청정기 작동
    # 위쪽
    for r in range(cleaner[0] - 1, 0, -1):
        house[r][0] = house[r - 1][0]
    for c in range(C - 1):
        house[0][c] = house[0][c + 1]
    for r in range(cleaner[0]):
        house[r][C - 1] = house[r + 1][C - 1]
    for c in range(C - 1, 1, -1):
        house[cleaner[0]][c] = house[cleaner[0]][c - 1]
    house[cleaner[0]][1] = 0

    # 아래쪽
    for r in range(cleaner[1] + 1, R - 1):
        house[r][0] = house[r + 1][0]
    for c in range(C - 1):
        house[R -1][c] = house[R - 1][c + 1]
    for r in range(R - 1, cleaner[1], -1):
        house[r][C - 1] = house[r - 1][C - 1]
    for c in range(C - 1, 1, -1):
        house[cleaner[1]][c] = house[cleaner[1]][c - 1]
    house[cleaner[1]][1] = 0

total = 2
for r in range(R):
    for c in range(C):
        total += house[r][c]
print(total)
