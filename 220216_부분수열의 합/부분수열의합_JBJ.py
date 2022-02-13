import sys

N = int(sys.stdin.readline().strip())
SEQUENCE = list(map(int, sys.stdin.readline().strip().split()))
sum_list = [True] + [False] * (20 * 10**5) # maximum number x maximum sequence length

def dfs(idx, prev_sum): # O(2^N) - 1
    if idx >= N:
        return
    new_sum = prev_sum + SEQUENCE[idx]
    
    sum_list[SEQUENCE[idx]] = True
    sum_list[prev_sum] = True
    sum_list[new_sum] = True
    
    dfs(idx + 1, new_sum) # addition
    dfs(idx + 1, prev_sum) # no addition

dfs(0, 0)
print(sum_list.index(False)) # minimum sum of subsequences
