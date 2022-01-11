'''
정수를 저장하는 큐 구현하기
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''


import sys

class Queue():
    def __init__(self):
        self.queue = list()

    def push(self, X):
        self.queue.append(X)

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return -1

    def size(self):
        return len(self.queue)

    def empty(self):
        return int(not self.queue)

    def front(self):
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def back(self):
        if self.queue:
            return self.queue[-1]
        else:
            return -1

# 내장 함수 input()은 여러줄 입력받을 때 시간초과 발생할 수 있음
# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
input = sys.stdin.readline
count = int(input())
commands = [input().strip() for _ in range(count)]

q = Queue()
cmd_dir = {
    'push': q.push,
    'pop': q.pop,
    'size': q.size,
    'empty': q.empty,
    'front': q.front,
    'back': q.back
}

for c in commands:    
    if c.startswith('push'):
        c, num = c.split()
        cmd_dir[c](num)
    else:
        result = cmd_dir[c]()
        print(result)
        