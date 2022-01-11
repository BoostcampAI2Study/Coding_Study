import sys
from collections import deque

def func1(cmd, queue):
    if "push" in cmd:        
        queue.append(cmd[5:])
    elif "pop" in cmd:
        if queue:
            print(queue.popleft())
        else: 
            print(-1)
    elif "size" in cmd:
        print(len(queue))
    elif "empty" in cmd:
        if queue:
            print(0)
        else:
            print(1)
    elif "front" in cmd:
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif "back" in cmd:
        if queue:
            print(queue[-1])
        else:
            print(-1)

queue=deque()

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    cmd = sys.stdin.readline().rstrip()
    func1(cmd,queue)