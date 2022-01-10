import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, data):
        if self.length == 0:
            self.head = Node(data)
            self.tail = self.head
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = Node(data)
            self.tail = cur.next

        self.length += 1

    def pop(self):
        if self.head is None:
            return -1
        else:
            head = self.head.data
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return head

    def size(self):
        return self.length

    def empty(self):
        if self.head is None:
            return 1
        else:
            return 0

    def front(self):
        if self.head is None:
            return -1
        return self.head.data

    def back(self):
        if self.tail is None:
            return -1
        return self.tail.data
        

cnt = int(input())
q = linkedList()

for _ in range(cnt):
    command = input()[:-1]
    ans = -1

    if 'push' in command:
        command, num = command.split()
        
        q.push(int(num))
        continue

    elif command == 'pop':
        ans = q.pop()

    elif command == 'size':
        ans = q.size()
    
    elif command == 'empty':
        ans = q.empty()

    elif command == 'front':
        ans = q.front()

    elif command == 'back':
        ans = q.back()

    print(ans)
