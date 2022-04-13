# https://www.acmicpc.net/problem/1806

import sys

input = sys.stdin.readline

N, S = map(int, input().split())
NUMS = list(map(int, input().split()))

answer = float("inf")
i, j = 0, 1
subtotal = NUMS[0]
while i < N:
    if j >= N:
        if subtotal < S:
            break
        else:
            answer = min(answer, j - i)
            subtotal -= NUMS[i]
            i += 1

    else:
        if i == j:
            subtotal = NUMS[i]
            j += 1
            if subtotal >= S:
                answer = 1

        else:
            if subtotal < S:
                subtotal += NUMS[j]
                j += 1
            else:
                answer = min(answer, j - i)
                subtotal -= NUMS[i]
                i += 1

print(answer if answer != float("inf") else 0)
