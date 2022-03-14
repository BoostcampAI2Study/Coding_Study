# reference: https://hibee.tistory.com/154 (부분수열의 합1)
# 부분수열의 합1은 itertools 사용해도 시간 초과가 나지 않았지만 2는 사용시 시간초과 발생 → dfs 사용

import sys, collections

N, S = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))
sum_cnt = collections.defaultdict(int)  # {sum:cnt}
res_cnt = 0

# front subsequence의 모든 sum에 대해서 cnt를 sum_cnt에 저장 → 부분 수열은 연속하는 수 X
def front_subseq_sum(idx, prev_sum):
    if idx == (N // 2):
        sum_cnt[prev_sum] += 1
        return
    front_subseq_sum(idx + 1, prev_sum)
    front_subseq_sum(idx + 1, prev_sum + sequence[idx])

# back subsequence
def back_subseq_sum(idx, prev_sum):
    global res_cnt
    if idx == N:
        res_cnt += sum_cnt[S - prev_sum]
        return
    back_subseq_sum(idx + 1, prev_sum)
    back_subseq_sum(idx + 1, prev_sum + sequence[idx])

front_subseq_sum(0,0)
back_subseq_sum(N//2, 0)

if S == 0:
    res_cnt -= 1  # 공집합 제외

print(res_cnt)
