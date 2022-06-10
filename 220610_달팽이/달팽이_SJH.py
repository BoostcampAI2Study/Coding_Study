from sys import stdin


input = stdin.readline
last = int(input())
find = int(input())


board = [[0] * last for _ in range(last)]

num = 1
count = -1
i = j = last // 2
last = last ** 2 + 1


board[i][j] = num
num += 1

coordinate = '' if find != 1 else f'{i+1} {j+1}'

while num < last:
    for _i, _j in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        count += 1
        for _ in range(count//2+1):
            if num == last:
                break
            i += _i
            j += _j
            board[i][j] = num

            if num == find:
                coordinate = f'{i+1} {j+1}'

            num += 1

        if num == last:
            break


for line in board:
    print(*line, sep=' ')

print(coordinate)
