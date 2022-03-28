import sys

N = int(sys.stdin.readline().rstrip())
SEQUENCE = list(map(int, sys.stdin.readline().rstrip().split()))
OP_COUNTS = list(map(int, sys.stdin.readline().rstrip().split())) # +, -, *, /
max_num, min_num = -(sys.maxsize), sys.maxsize

def dfs(seq_idx, cur_sum):
    global SEQUENCE, OP_COUNTS, max_num, min_num

    if seq_idx >= len(SEQUENCE):
        max_num, min_num = max(max_num, cur_sum), min(min_num, cur_sum)
    else:
        if OP_COUNTS[0]: # '+' operation
            OP_COUNTS[0] -= 1
            dfs(seq_idx+1, cur_sum + SEQUENCE[seq_idx])
            OP_COUNTS[0] += 1
        if OP_COUNTS[1]: # '-' operation
            OP_COUNTS[1] -= 1
            dfs(seq_idx+1, cur_sum - SEQUENCE[seq_idx])
            OP_COUNTS[1] += 1
        if OP_COUNTS[2]: # '*' operation
            OP_COUNTS[2] -= 1
            dfs(seq_idx+1, cur_sum * SEQUENCE[seq_idx])
            OP_COUNTS[2] += 1
        if OP_COUNTS[3]: # '/' operation
            OP_COUNTS[3] -= 1
            dfs(seq_idx+1, int(cur_sum / SEQUENCE[seq_idx]))
            OP_COUNTS[3] += 1

dfs(1, SEQUENCE[0])
print(max_num, min_num)