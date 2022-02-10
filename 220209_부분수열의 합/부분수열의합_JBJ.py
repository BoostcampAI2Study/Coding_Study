import sys

N, S = map(int, sys.stdin.readline().strip().split())
SEQUENCE = list(map(int, sys.stdin.readline().strip().split()))
s_cnt = 0

def dfs(idx, prev_sum): # O(2^N) - 1
    global s_cnt
    if idx >= N:
        return
    new_sum = prev_sum + SEQUENCE[idx]
    
    if new_sum == S:
        s_cnt += 1
        
    dfs(idx + 1, new_sum) # addition
    dfs(idx + 1, prev_sum) # no addition

dfs(0, 0)
print(s_cnt)
