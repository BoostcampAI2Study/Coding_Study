import collections, sys
S, T = map(int, sys.stdin.readline().strip().split())
    
if S == T:
    print('0')
else:
    calculated_numbers, answer = set([S]), -1
    Q = collections.deque()
    Q.append((S, ''))
    
    while Q:
        num, operation_order = Q.popleft()
        if num == T:
            answer = operation_order
            break
        
        for op in ['*', '+', '/']:    # because you want a number bigger than 0, '-' operation is unnecessary.
            new_num = int(eval(str(num) + op + str(num)))
            if 0 < new_num <= T and new_num not in calculated_numbers:
                calculated_numbers.add(new_num)
                Q.append((new_num, operation_order + op))
    
    print(answer)