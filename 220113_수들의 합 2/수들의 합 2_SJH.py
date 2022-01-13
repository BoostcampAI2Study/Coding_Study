'''
숫자가 N개 있는 수열에서 i부터 j까지 더했을때 M 나오는 경우의 수
'''
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0

for i in range(N):
    j = i+1
    _sum = sum(nums[i:j])
    if _sum == M:
        answer += 1

    while j < N:
        _sum += nums[j]
        if _sum == M:
            answer += 1
        j += 1

print(answer)
