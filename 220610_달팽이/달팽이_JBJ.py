N, PRINT_NUM = int(input()), int(input())
print_coordinate = f'{(N//2)+1} {(N//2)+1}'

SNAIL = [[0]*N for _ in range(N)]
SNAIL[N//2][N//2] = '1'

num = N**2
for i in range(N//2):
    for j in range(i, N-1-i):
        if num == PRINT_NUM: print_coordinate = f'{j+1} {i+1}'
        SNAIL[j][i] = str(num)
        num -= 1

    for j in range(i, N-1-i):
        if num == PRINT_NUM: print_coordinate = f'{(N-1-i)+1} {j+1}'
        SNAIL[N-1-i][j] = str(num)
        num -= 1
    
    for j in range(N-1-i, i, -1):
        if num == PRINT_NUM: print_coordinate = f'{j+1} {(N-1-i)+1}'
        SNAIL[j][N-1-i] = str(num)
        num -= 1

    for j in range(N-1-i, i, -1):
        if num == PRINT_NUM: print_coordinate = f'{i+1} {j+1}'
        SNAIL[i][j] = str(num)
        num -= 1

list(map(lambda x: print(' '.join(x)), SNAIL))
print(print_coordinate)