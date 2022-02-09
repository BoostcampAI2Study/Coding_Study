from collections import deque

s, t = map(int, input().split())

def mul(num):
    return num * num if num < t else -1

def add(num):
    return num * 2 if num < t else -1

def sub(num):
    return 0

def div(num):
    return 1

op_dict = {'*': mul, '+': add, '-': sub, '/': div}


if s == t:
    print(0)

else:
    queue = deque([('', s)])
    count = 0
    answer = -1
    check = set()

    while queue and count < 1e5:
        exp, s = queue.popleft()        
        op_order = list(op_dict.keys())

        if s == t:
            answer = exp
            break

        for op in op_order:
            _exp = exp + op
            _s = op_dict[op](s)
            
            if _s <= 0 or _s in check:
                continue

            queue.append((_exp, _s))
            check.add(_s)
            

        count += 1


    print(answer)