import sys

N, M = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))

answer = 0
left_ptr, right_ptr = 0, 1

while right_ptr <= len(nums):
    sliced_sum = sum(nums[left_ptr:right_ptr])

    if sliced_sum > M: # decrease sum by moving left_ptr.
        left_ptr += 1
    else: # increase sum by moving right_ptr.
        if sliced_sum == M:
            answer += 1
        right_ptr += 1

print(answer)