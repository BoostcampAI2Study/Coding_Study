import sys


class Queue():
    def __init__(self):
        self._queue = []
    
    def push(self, x):
        self._queue.append(x)
    
    def pop(self):
        if self._queue:
            ret_value = self._queue[0]
            del self._queue[0] # https://brownbears.tistory.com/452

            return ret_value
        return -1
    
    def size(self):
        return len(self._queue)
    
    def empty(self):
        return False if self._queue else True
    
    def front(self):
        return self._queue[0] if self._queue else -1
    
    def back(self):
        return self._queue[-1] if self._queue else -1
        
        
N = int(sys.stdin.readline())
operations = [sys.stdin.readline().strip() for _ in range(N)]
Q = Queue()

for operation in operations:
    if operation == 'front':
        print(Q.front())
    elif operation == 'back':
        print(Q.back())
    elif operation == 'size':
        print(Q.size())
    elif operation == 'empty':
        print(int(Q.empty()))
    elif operation == 'pop':
        print(Q.pop())
    else:
        op, x = operation.split()
        if op == 'push':
            Q.push(int(x))
    
