import sys
from collections import deque

n = int(input())
q = deque()
for _ in range(n):
    commands = sys.stdin.readline().strip().split()
    c = commands[0]
    if c == 'push':
        q.append(commands[1])
    elif c == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif c == 'size':
        print(len(q))
    elif c == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif c == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)
