import sys

input = sys.stdin.readline

# 명령의 수 N
N = int(input())

# N번 명령어 입력
commands = []
for _ in range(N):
    commands.append(input())

# 명령어 순서대로 처리
queue = []
for command in commands:
    com = command.split()
    if com[0] == 'push':
        queue.append(com[1])
    elif com[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.pop(0))
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif com[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif com[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])