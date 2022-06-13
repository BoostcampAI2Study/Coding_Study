from sys import stdin


input = stdin.readline

length = int(input())
nums = list(map(int, input().split()))


lcs = [[0] * length for _ in range(length)]

for i in range(length):
    
    start = nums[i]

    for j in range(length):
        end = nums[length - 1 - j]

        if start == end:
            lcs[i][j] = 1

            if i > 0 and j > 0:
                lcs[i][j] += lcs[i-1][j-1]

        else:
            up = lcs[i-1][j] if i > 0 else 0
            left = lcs[i][j-1] if j > 0 else 0
            lcs[i][j] = max(up, left)


print(length - lcs[-1][-1])
