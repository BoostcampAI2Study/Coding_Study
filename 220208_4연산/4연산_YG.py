import sys
from collections import deque

input = sys.stdin.readline

S, T = map(int, input().split())

if S == T:
    print(0)
    sys.exit()

q = deque()

ans = []

q = deque()

q.append((S, "", 0))
q.append((0, "-", 1))
q.append((1, "/", 1))

last_level = 1e9
while q:
    number, operation, level = q.popleft()

    if number == T:
        ans.append(operation)
        last_level = min(last_level, level)
        continue

    if level >= last_level:
        continue

    # +
    if 2*number <= T and number != 0:
        q.append((2*number, operation+"+", level+1))


    # *
    if number**2 <= T and number != 0 and number != 1:
        q.append((number**2, operation+"*", level+1))



if ans:
    ans2 = []
    for a in ans:
        if len(a) == last_level:
            ans2.append(a)
    ans2.sort()
    print(ans2[0])
else:
    print(-1)