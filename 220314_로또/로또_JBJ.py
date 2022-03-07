import itertools, sys


"""
    PS 1: typical dfs [memory: 32396KB, time: 1608ms]
"""
def dfs(lotto_idx, lotto_nums):
    global K, S, lotto_cases
    
    if lotto_idx >= 6:
        lotto = tuple(sorted(list(lotto_nums)))
        if lotto not in lotto_cases:
            lotto_cases.add(lotto)
        return

    for num in S:
        if num not in lotto_nums:
            dfs(lotto_idx+1, lotto_nums | set([num]))

EMTPY_LINE_FLAG = False # memory efficient way
while True:
    LINE = list(map(int, sys.stdin.readline().strip().split()))
    if LINE[0] == 0: break

    if EMTPY_LINE_FLAG:
        print()
    else:
        EMTPY_LINE_FLAG = True
        
    K, S, lotto_cases = LINE[0], set(LINE[1:]), set()
    dfs(0, set())

    for lotto in sorted(lotto_cases):
        print(' '.join(map(str, lotto)))


"""
    PS 2: optimized dfs with ordering [memory: 32396KB, time: 92ms]
"""
def dfs(num_idx, lotto_nums):
    global K, S, lotto_cases
    len_lotto_nums = len(lotto_nums)

    if len_lotto_nums == 6:
        lotto_cases.add(tuple(lotto_nums))
        return

    for next_num_idx in range(num_idx+1, K):
        # '# of remained candidates' should be greater than or equal to '# of remained picks'.
        if K - next_num_idx >= 6 - len_lotto_nums:   
            dfs(next_num_idx, lotto_nums + [S[next_num_idx]])

EMTPY_LINE_FLAG = False # memory efficient way
while True:
    LINE = list(map(int, sys.stdin.readline().strip().split()))
    if LINE[0] == 0: break
    if EMTPY_LINE_FLAG:
        print()
    else:
        EMTPY_LINE_FLAG = True

    K, S, lotto_cases = LINE[0], sorted(LINE[1:]), set()
    for idx, num in enumerate(S[:(K-6)+1]):
        dfs(idx, [num])

    for lotto in sorted(lotto_cases):
        print(' '.join(map(str, lotto)))


"""
    PS 3: itertools.combinations [memory: 32372KB, time: 92ms]
"""
EMTPY_LINE_FLAG = False # memory efficient way 
while True:
    LINE = list(map(int, sys.stdin.readline().strip().split()))
    if LINE[0] == 0: break

    if EMTPY_LINE_FLAG:
        print()
    else:
        EMTPY_LINE_FLAG = True

    K, S = LINE[0], sorted(LINE[1:])
    lotto_cases = itertools.combinations(S, 6)

    for lotto in sorted(lotto_cases):
        print(' '.join(map(str, lotto)))