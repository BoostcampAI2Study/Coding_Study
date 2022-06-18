import sys
def get_teleport(x, y):
    near_city, min_dist = -1, 1e9
    for i in special_cities:
        _, tx, ty = CITIES[i]
        distance = abs(tx - x) + abs(ty - y)
        if min_dist > distance:
            near_city, min_dist = i, distance
    return near_city

N, T = map(int, sys.stdin.readline().split())
CITIES = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
M = int(sys.stdin.readline())
CITY_PAIRS = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

special_cities = [i for i in range(len(CITIES)) if CITIES[i][0]]
for city1, city2 in CITY_PAIRS:
    [s1, x1, y1], [s2, x2, y2] = CITIES[city1 - 1], CITIES[city2 - 1]
    n1, n2 = get_teleport(x1, y1), get_teleport(x2, y2)
    print(min(abs(x1 - x2) + abs(y1 - y2), T + abs(x1 - CITIES[n1][1]) + abs(y1 - CITIES[n1][2]) + abs(x2 - CITIES[n2][1]) + abs(y2 - CITIES[n2][2])))
