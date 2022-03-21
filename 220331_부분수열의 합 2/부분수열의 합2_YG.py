# ref: https://peisea0830.tistory.com/40
from collections import defaultdict
from itertools import combinations
import sys
input = sys.stdin.readline

N, S = map(int, input().split())

arr = list(map(int, input().split()))

subset_1, subset_2 = arr[:(N//2)+1], arr[(N//2)+1:]

sum_1 = []
for idx in range(len(subset_1)+1):
    for k in list(combinations(subset_1, idx)):
        sum_1.append(sum(k))
sum_2 = []
for idx in range(len(subset_2)+1):
    for k in list(combinations(subset_2, idx)):
        sum_2.append(sum(k))

# 정렬
sum_1.sort()
sum_2.sort(reverse=True)
n_1, n_2 = len(sum_1), len(sum_2)

# 탐색
left_idx = 0
right_idx = 0
answer = 0

while left_idx < n_1 and right_idx < n_2:
    value = sum_1[left_idx]+sum_2[right_idx]

    # index 옮기기
    if value == S:
        left_idx += 1
        right_idx += 1
        cnt_1 = 1
        cnt_2 = 1
        while left_idx < n_1 and sum_1[left_idx] == sum_1[left_idx-1]:
            cnt_1 += 1
            left_idx += 1
        while right_idx < n_2 and sum_2[right_idx] == sum_2[right_idx-1]:
            cnt_2 += 1
            right_idx += 1
        answer += (cnt_1*cnt_2)
    elif value < S:
        left_idx += 1
    else:
        right_idx += 1


if S == 0:
    answer -= 1

print(answer)



