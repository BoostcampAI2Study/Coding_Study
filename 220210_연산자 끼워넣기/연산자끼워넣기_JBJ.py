import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline().strip())
SEQUENCE = list(map(int, sys.stdin.readline().strip().split()))
OPERATOR_CNTS = list(map(int, sys.stdin.readline().strip().split()))
max_result, min_result = -sys.maxsize, sys.maxsize

def dfs(sequence_idx, cur_result, operator_cnts): # O(N!) - O(10!)
    global N, SEQUENCE, max_result, min_result
    if sequence_idx >= N:
        max_result, min_result = max(max_result, cur_result), min(min_result, cur_result)
        return
    
    for op_idx, op_cnt in enumerate(operator_cnts):
        if op_cnt:
            if op_idx == 0:
                new_result = cur_result + SEQUENCE[sequence_idx]
            elif op_idx == 1:
                new_result = cur_result - SEQUENCE[sequence_idx]
            elif op_idx == 2:
                new_result = cur_result * SEQUENCE[sequence_idx]
            else:
                new_result = int(cur_result / SEQUENCE[sequence_idx])
            
            operator_cnts[op_idx] -= 1
            dfs(sequence_idx+1, new_result, operator_cnts)
            operator_cnts[op_idx] += 1
            
dfs(1, SEQUENCE[0], OPERATOR_CNTS)
print(max_result, min_result)