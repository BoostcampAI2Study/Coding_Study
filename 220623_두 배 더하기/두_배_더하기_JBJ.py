N, B = int(input()), list(map(int, input().split()))
min_total_op_cnt = 0

while True:
    new_b = []
    for b in B:
        if b%2: # the number is odd.
            b -= 1
            min_total_op_cnt += 1
        new_b.append(b)
    
    if sum(new_b) == 0:
        break
    else: # all of the numbers in B are even.
        B = [b//2 for b in new_b]
        min_total_op_cnt += 1
        
print(min_total_op_cnt)
