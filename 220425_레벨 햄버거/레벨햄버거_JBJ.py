N, X = map(int, input().rstrip().split())

TOTAL_LENGTHS, PATTY_CNTS = [1], [1]
for idx in range(N):
    TOTAL_LENGTHS.append((TOTAL_LENGTHS[idx]*2)+3) # bun | lv(L-1) burger | patty | lv(L-1) burger | bun
    PATTY_CNTS.append((PATTY_CNTS[idx]*2)+1)

def get_eaten_patties_cnt(n, x):
    global TOTAL_LENGTHS, PATTY_CNTS
    middle = (TOTAL_LENGTHS[n]//2)+1
    
    if x == 0: # 0-th
        return 0
    elif x == TOTAL_LENGTHS[n]: # whole layer
        return PATTY_CNTS[n]
    elif x == 1: # first layer - lv(0): patty, lv(1~): bun
        return 0 if n else 1
    elif x < middle: # {{ bun | lv(L-1) burger }} | patty | lv(L-1) burger | bun
        return get_eaten_patties_cnt(n-1, x-1) 
    elif x == middle: # {{ bun | lv(L-1) burger | patty }} | lv(L-1) burger | bun
        return PATTY_CNTS[n-1]+1
    elif x > middle: # {{ bun | lv(L-1) burger | patty | lv(L-1) burger | bun }}
        return PATTY_CNTS[n-1]+1 + get_eaten_patties_cnt(n-1, x-middle) 

print(get_eaten_patties_cnt(N, X))