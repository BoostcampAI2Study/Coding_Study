import collections

N, S = map(int, input().rstrip().split())
SEQUENCE = list(map(int, input().rstrip().split()))
MID = N // 2
LEFT_SUBSEQ_SUM_CNT, RIGHT_SUBSEQ_SUM_CNT = collections.defaultdict(int), collections.defaultdict(int)

def dfs(idx, prev_sum):
    global SEQUENCE, LEFT_SUBSEQ_SUM_CNT, RIGHT_SUBSEQ_SUM_CNT, N, MID

    if idx < MID:
        LEFT_SUBSEQ_SUM_CNT[prev_sum + SEQUENCE[idx]] += 1
        if idx+1 == MID: return
    else:
        RIGHT_SUBSEQ_SUM_CNT[prev_sum + SEQUENCE[idx]] += 1
        if idx+1 == N: return

    dfs(idx+1, prev_sum)
    dfs(idx+1, prev_sum + SEQUENCE[idx])

if N >= 2:
    LEFT_SUBSEQ_SUM_CNT[0], RIGHT_SUBSEQ_SUM_CNT[0] = 1, 1 # no select case count
    dfs(0, 0)
    dfs(MID, 0)

    LEFT_SUBSEQ_SUM, RIGHT_SUBSEQ_SUM = sorted(LEFT_SUBSEQ_SUM_CNT.keys()), sorted(RIGHT_SUBSEQ_SUM_CNT.keys())
    answer, left_idx, right_idx = 0, 0, len(RIGHT_SUBSEQ_SUM)-1

    while left_idx < len(LEFT_SUBSEQ_SUM) and right_idx >= 0: # LEFT: ascending, RIGHT: descending
        left_num, right_num = LEFT_SUBSEQ_SUM[left_idx], RIGHT_SUBSEQ_SUM[right_idx]
        if left_num + right_num == S:
            answer += (LEFT_SUBSEQ_SUM_CNT[left_num] * RIGHT_SUBSEQ_SUM_CNT[right_num])
            left_idx += 1
            right_idx -= 1
        elif left_num + right_num > S:
            right_idx -= 1
        else:
            left_idx += 1

    print(answer-1 if S == 0 else answer) # LEFT no select case + RIGHT no select case == 1
else:
    print(1 if SEQUENCE[0] == S else 0)