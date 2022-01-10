import sys
def solution(input):
    queue = []

    for order in input[1:]:
        order = order.strip('\n')
        if "push" in order:
            num = int(order.split()[1])
            queue.append(num)
        elif order == "pop":
            print(queue.pop(0)) if len(queue)!=0 else print(-1)
        elif order == "size":
            print(len(queue))
        elif order == "empty":
            print(1) if len(queue)==0 else print(0)
        elif order == "front":
            print(queue[0]) if len(queue)!=0 else print(-1)
        elif order == "back":
            print(queue[-1]) if len(queue)!=0 else print(-1)

input = sys.stdin.readlines()
solution(input)

