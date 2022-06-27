# https://www.acmicpc.net/problem/12931

import sys

input = sys.stdin.readline


N = int(input())
goal = list(map(int, input().split()))

zero_set = set()
odd_cnt = 0
while len(zero_set) < N:
    for i in range(len(goal)):
        if goal[i] % 2 == 1:
            odd_cnt += 1
            goal[i] = (goal[i] - 1) // 2
        else:
            goal[i] = goal[i] // 2
        if goal[i] == 0:
            zero_set.add(i)
    if len(zero_set) < N:
        odd_cnt += 1
print(odd_cnt)
