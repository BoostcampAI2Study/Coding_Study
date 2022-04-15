import sys
N = int(sys.stdin.readline())
MAPS = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def get_boundary(point_r, point_c, d1, d2):
    election_district = [[0] * N for _ in range(N)]
    populations = [0] * 5

    # set 5th election district
    for i in range(d1 + 1):
        election_district[point_r + i][point_c - i] = 5
        election_district[point_r + d2 + i][point_c + d2 - i] = 5

    for i in range(d2 + 1):
        election_district[point_r + i][point_c + i] = 5
        election_district[point_r + d1 + i][point_c - d1 + i] = 5

    for r in range(point_r + 1, point_r + d1 + d2):
        is_start = False
        for c in range(N):
            if is_start and election_district[r][c + 1] == 5:
                break
            if election_district[r][c] == 5:
                election_district[r][c + 1] = 5
                if not is_start:
                    is_start = True
    # count each election districts population
    for r in range(N):
        for c in range(N):
            if not election_district[r][c]:
                if 0 <= r < point_r + d1 and 0 <= c <= point_c:
                    populations[0] += MAPS[r][c]
                elif 0 <= r <= point_r + d2 and point_c < c < N:
                    populations[1] += MAPS[r][c]
                elif point_r + d1 <= r < N and 0 <= c < point_c - d1 + d2:
                    populations[2] += MAPS[r][c]
                elif point_r + d2 < r < N and point_c - d1 + d2 <= c < N:
                    populations[3] += MAPS[r][c]
            else:
                populations[4] += MAPS[r][c]
    return max(populations) - min(populations)

min_result = 1e9
for r in range(N - 1):
    for c in range(N - 1):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if 0 <= r < r + d1 + d2 < N and 0 <= c - d1 < c < c + d2 < N:
                    min_result = min(min_result, get_boundary(r, c, d1, d2))

print(min_result)
