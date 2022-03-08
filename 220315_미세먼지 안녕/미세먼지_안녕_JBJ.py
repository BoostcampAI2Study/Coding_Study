import collections, sys

R, C, T = map(int, sys.stdin.readline().strip().split())
MAP = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(R)]
DR = [0, 0, 1, -1]
DC = [1, -1, 0, 0]

# Initialization
AIR_CLEANER, dust = list(), set()
for r in range(R):
    for c in range(C):
        if MAP[r][c] == -1:
            AIR_CLEANER.append((r, c))
        if MAP[r][c] > 0:
            dust.add((r, c))

def air_cleaning(r, c, is_clockwise):
    global AIR_CLEANER, dust, DR, DC, MAP, R
    if is_clockwise:
        wind_blow_direction = (0, 2, 1, 3) # right, down, left, up
        MIN_R, MAX_R = AIR_CLEANER[1][0], R
    else:
        wind_blow_direction = (0, 3, 1, 2) # right, up, left, down
        MIN_R, MAX_R = 0, AIR_CLEANER[0][0]+1
    buffer = 0
    
    for idx in range(4):
        r, c = r + DR[wind_blow_direction[idx]], c + DC[wind_blow_direction[idx]]
        while True:
            if buffer:
                dust.add((r, c))
            elif not buffer and (r, c) in dust:
                dust.remove((r, c)) 

            MAP[r][c], buffer = buffer, MAP[r][c]

            if MIN_R <= r + DR[wind_blow_direction[idx]] < MAX_R and 0 <= c + DC[wind_blow_direction[idx]] < C:
                r, c = r + DR[wind_blow_direction[idx]], c + DC[wind_blow_direction[idx]]
                if (r, c) in AIR_CLEANER: return
            else:
                break

for _ in range(T):
    # 1. spreading dust.
    new_dust = collections.defaultdict(int)
    for dust_r, dust_c in dust:
        spread = MAP[dust_r][dust_c] // 5
        if spread:
            for idx in range(4):
                new_dust_r, new_dust_c = dust_r + DR[idx], dust_c + DC[idx]
                if 0 <= new_dust_r < R and 0 <= new_dust_c < C and (new_dust_r, new_dust_c) not in AIR_CLEANER:
                    new_dust[(new_dust_r, new_dust_c)] += spread
                    MAP[dust_r][dust_c] -= spread

    for (new_dust_r, new_dust_c), new_dust_amount in new_dust.items():
        MAP[new_dust_r][new_dust_c] += new_dust_amount
    dust |= set(new_dust.keys())
    
    # 2. functioning the air cleaner.
    air_cleaning(r=AIR_CLEANER[0][0], c=0, is_clockwise=False) # counter-clockwise => upper part
    air_cleaning(r=AIR_CLEANER[1][0], c=0, is_clockwise=True)  # clockwise => lower part

print(sum(map(sum, MAP))+2) # air cleaner: -2