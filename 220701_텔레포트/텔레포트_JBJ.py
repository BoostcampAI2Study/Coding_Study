import sys

N, T = map(int, sys.stdin.readline().split())
COST_MATRIX = [[0]*(N) for _ in range(N)]
CITIES = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for city in range(N):
    for adj_city in range(N):
        if adj_city != city:
            cost = abs(CITIES[city][1] - CITIES[adj_city][1]) + abs(CITIES[city][2] - CITIES[adj_city][2])
            COST_MATRIX[city][adj_city], COST_MATRIX[adj_city][city] = cost, cost
            if CITIES[city][0] == CITIES[adj_city][0] == 1 and T < cost:
                COST_MATRIX[city][adj_city], COST_MATRIX[adj_city][city] = T, T
                
def get_min_teleportable_city_and_distance(city):
    teleportable_cities, min_distance = set(), sys.maxsize
    for adj_city in range(N):
        if CITIES[adj_city][0] == 0: continue
        else:
            if min_distance > COST_MATRIX[city][adj_city]:
                teleportable_cities = set()
                teleportable_cities.add(adj_city)
                min_distance = COST_MATRIX[city][adj_city]
            elif min_distance == COST_MATRIX[city][adj_city]: 
                teleportable_cities.add(adj_city) # for a case of stopping by the same teleportable city.

    return teleportable_cities, min_distance

def get_min_distance(a_city, b_city):
    min_distance = COST_MATRIX[a_city][b_city] # direct distance
    if CITIES[a_city][0] == CITIES[b_city][0] == 1: 
        return min_distance
    else:
        a_teleportable_cities, a_min_distance = get_min_teleportable_city_and_distance(a_city)
        b_teleportable_cities, b_min_distance = get_min_teleportable_city_and_distance(b_city)
        return min(min_distance, (a_min_distance + b_min_distance) if a_teleportable_cities & b_teleportable_cities else (a_min_distance + b_min_distance + T))

M = int(sys.stdin.readline())
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    print(get_min_distance(A-1, B-1))