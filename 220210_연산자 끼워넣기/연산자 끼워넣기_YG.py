from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

operation = list(map(int, input().split()))

q = deque()

q.append((0, arr[0], operation[0], operation[1], operation[2], operation[3]))

answer = []
while q:
    level, value, plus, minus, mul, divide = q.popleft()

    if level == N-1:
        answer.append(value)
        continue

    if plus >= 1:
        q.append((level+1, value+arr[level+1], plus-1, minus, mul, divide))

    if minus >= 1:
        q.append((level+1, value-arr[level+1], plus, minus-1, mul, divide))

    if mul >= 1:
        q.append((level+1, value*arr[level+1], plus, minus, mul-1, divide))

    if divide >= 1:
        if value < 0:
            q.append((level+1, -((-value)//arr[level+1]), plus, minus, mul, divide-1))
        else:
            q.append((level+1, value//arr[level+1], plus, minus, mul, divide-1))

answer.sort()
print(answer[-1])
print(answer[0])