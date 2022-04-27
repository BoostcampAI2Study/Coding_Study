import sys

def get_min_diff_population(base_y, base_x, d1, d2):
    global A, N, TOTAL_POPULATION

    boundaries = set([(base_y, base_x)])
    for i in range(1, d1+1):
        boundaries.add((base_y+i, base_x-i)) # district 1 boundaries
        boundaries.add(((base_y+d2)+i, (base_x+d2)-i)) # district 4 boundaries
    for i in range(1, d2+1):
        boundaries.add((base_y+i, base_x+i)) # district 2 boundaries
        boundaries.add(((base_y+d1)+i, (base_x-d1)+i)) # district 3 boundaries

    districts_population = [0, 0, 0, 0]
    for y in range(base_y+d1): # district 1 population
        for x in range(base_x+1):
            if (y, x) in boundaries: break
            districts_population[0] += A[y][x]
    for y in range(base_y+d2+1): # district 2 population
        for x in range(N-1, base_x, -1):
            if (y, x) in boundaries: break
            districts_population[1] += A[y][x]
    for y in range(base_y+d1, N): # district 3 population
        for x in range(base_x-d1+d2):
            if (y, x) in boundaries: break
            districts_population[2] += A[y][x]
    for y in range(base_y+d2+1, N): # district 4 population
        for x in range(N-1, base_x-d1+d2-1, -1):
            if (y, x) in boundaries: break
            districts_population[3] += A[y][x]
    
    district_5 = TOTAL_POPULATION - sum(districts_population)

    return max(district_5, max(districts_population)) - min(district_5, min(districts_population))

N = int(sys.stdin.readline().rstrip())
A = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
TOTAL_POPULATION = sum(map(sum, A))

min_diff_population = 1e9
for y in range(N-2): # row
    for x in range(1, N-1): # column
        for d1 in range(1, N-1):
            for d2 in range(1, N-d1):
                if y+d1+d2 < N and 0 <= x-d1 and x+d2 < N: # rectangle sanity check.
                    min_diff_population = min(min_diff_population, get_min_diff_population(y, x, d1, d2))

print(min_diff_population)