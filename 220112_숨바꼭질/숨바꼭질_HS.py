class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = Node(None)
        self.back = Node(None)
        self.size = 0

    def _front(self):
        if self.front.next:
            return self.front.next.value
        return -1

    def _back(self):
        if self.back.next:
            return self.back.next.value
        return -1

    def push(self, value):
        node = Node(value)
        if self.front.next != None:
            self.front.next.next = node
        self.front.next = node
        if self.back.next == None:
            self.back.next = node
        self.size += 1
        return value

    def pop(self):
        if self.size == 0:
            return -1
        value = self.back.next.value
        self.back.next = self.back.next.next
        self.size -= 1
        if self.size == 0:
            self.front.next  = None
        return value

    def _size(self):
        return self.size

    def empty(self):
        if self.size:
            return 0
        return 1

q = Queue()
n = int(input())
for i in range(n):
    command = input().split()
    if command[0][0] != command[-1][0]:
        q.push(int(command[-1]))
    elif command[-1] == 'pop':
        print(q.pop())
    elif command[-1] == 'front':
        print(q._back())
    elif command[-1] == 'back':
        print(q._front())
    elif command[-1] == 'size':
        print(q._size())
    elif command[-1] == 'empty':
        print(q.empty())
        