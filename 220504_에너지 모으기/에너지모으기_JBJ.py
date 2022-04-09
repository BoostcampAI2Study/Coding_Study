N = int(input().rstrip())
MARBLES = list(map(int, input().rstrip().split()))

def dfs():
    global MARBLES

    if len(MARBLES) == 3:
        return MARBLES[0] * MARBLES[2]
    
    max_energy_sum = 0
    for idx in range(1, len(MARBLES)-1):
        energy_sum, energy = MARBLES[idx-1] * MARBLES[idx+1], MARBLES[idx]

        del MARBLES[idx] # eliminate energy.
        total_energy_sum = energy_sum + dfs()
        max_energy_sum = max(max_energy_sum, total_energy_sum)
        MARBLES.insert(idx, energy) # restore energy.
    return max_energy_sum

print(dfs())