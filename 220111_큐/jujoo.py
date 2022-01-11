from collections import deque
class Queue:
    def __init__(self):
        self.q = deque()
    def push(self, num):
        self.q.append(num)
    def pop(self):
        if self.q:
            print(self.q.popleft())
        else:
            print(-1)
    def size(self):
        print(len(self.q))
    def empty(self):
        if self.q:
            print(0)
        else:
            print(1)
    def front(self):
        if self.q:
            print(self.q[0])
        else:
            print(-1)
    def back(self):
        if self.q:
            print(self.q[-1])
        else:
            print(-1)
 
if __name__ == '__main__':
    q = Queue()
    N = int(input())
    cmds = [list(input().split()) for _ in range(N)]
    for cmd in cmds:
        if cmd[0] == 'push':
            q.push(int(cmd[1]))
        elif cmd[0] == 'pop':
            q.pop()
        elif cmd[0] == 'size':
            q.size()
        elif cmd[0] == 'empty':
            q.empty()
        elif cmd[0] == 'front':
            q.front()
        elif cmd[0] == 'back':
            q.back()