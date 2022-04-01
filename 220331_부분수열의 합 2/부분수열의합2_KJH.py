# https://www.acmicpc.net/problem/1208

from collections import defaultdict
from itertools import combinations


N, S = map(int, input().split())
nums_list = list(map(int, input().split()))
nums_list.sort()

MID = N // 2
LEFT_SUM_SETS_CNT, RIGHT_SUM_SETS_CNT = defaultdict(int), defaultdict(int)


def cnt_subset(sub_numlist, isleft):
    if isleft:
        LEFT_SUM_SETS_CNT[0] = 1
    else:
        RIGHT_SUM_SETS_CNT[0] = 1
    for i in range(1, len(sub_numlist) + 1):
        for sub in combinations(sub_numlist, i):
            if isleft:
                LEFT_SUM_SETS_CNT[sum(sub)] += 1
            else:
                RIGHT_SUM_SETS_CNT[sum(sub)] += 1


cnt_subset(nums_list[:MID], True)
cnt_subset(nums_list[MID:], False)
LEFT_SUM_SET, RIGHT_SUM_SET = sorted(LEFT_SUM_SETS_CNT.keys()), sorted(
    RIGHT_SUM_SETS_CNT.keys()
)
left_idx, right_idx = 0, len(RIGHT_SUM_SET) - 1
answer = 0
while left_idx < len(LEFT_SUM_SET) and right_idx >= 0:
    if LEFT_SUM_SET[left_idx] + RIGHT_SUM_SET[right_idx] == S:
        answer += (
            LEFT_SUM_SETS_CNT[LEFT_SUM_SET[left_idx]]
            * RIGHT_SUM_SETS_CNT[RIGHT_SUM_SET[right_idx]]
        )
        right_idx -= 1
        left_idx += 1
    elif LEFT_SUM_SET[left_idx] + RIGHT_SUM_SET[right_idx] > S:
        right_idx -= 1
    else:
        left_idx += 1

print(answer - 1 if S == 0 else answer)
