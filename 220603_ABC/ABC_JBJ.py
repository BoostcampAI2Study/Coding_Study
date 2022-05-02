N, K = map(int, input().rstrip().split())
dp = [[[[False]*436 for _ in range(31)] for _ in range(31)] for _ in range(31)]
S = ['']*N

def is_satisfying(str_len, a_cnt, b_cnt, pair_cnt):
    global N, K, dp

    if str_len == N:
        if pair_cnt == K: return True
        else: return False
    
    if dp[str_len][a_cnt][b_cnt][pair_cnt]: return False # already visited; this string does not satisfy the conditions.
    else: dp[str_len][a_cnt][b_cnt][pair_cnt] = True # visit check.
    
    S[str_len] = 'A'
    if is_satisfying(str_len+1, a_cnt+1, b_cnt, pair_cnt): return True

    S[str_len] = 'B'
    if is_satisfying(str_len+1, a_cnt, b_cnt+1, pair_cnt+a_cnt): return True

    S[str_len] = 'C'
    if is_satisfying(str_len+1, a_cnt, b_cnt, pair_cnt+a_cnt+b_cnt): return True

    return False

print(''.join(S) if is_satisfying(0, 0, 0, 0) else -1)
