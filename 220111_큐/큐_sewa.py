import sys

queue = []
N = int(input())

commands = [sys.stdin.readline().split() for _ in range(N)]


for command in commands:
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        print(-1) if not queue else print(queue.pop[0])
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(0) if queue else print(1)
    elif command[0] == 'front':
        print(queue[0]) if queue else print(-1)
    elif command[0] == 'back':
        print(queue[-1]) if queue else print(-1)
