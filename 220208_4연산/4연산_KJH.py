# https://www.acmicpc.net/problem/14395

from collections import deque


S, T = map(int, input().split())

visited = set()


def bfs():
    global S, T
    q = deque([(S, "")])
    while q:
        num, op = q.popleft()
        if num in visited:
            continue
        if S < T:
            if num > T:
                continue
        else:
            if num != S and num > T:
                continue

        if num == T:
            return op

        visited.add(num)
        for oper in "*+-/":
            if oper == "/" and num == 0:
                continue
            if oper == "*":
                next_num = num * num
            elif oper == "+":
                next_num = num + num
            elif oper == "-":
                next_num = num - num
            elif oper == "/":
                next_num = num / num

            if next_num not in visited:
                q.append((next_num, op + oper))
    return -1


if S == T:
    print(0)
else:
    print(bfs())
