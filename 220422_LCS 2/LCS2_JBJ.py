STRING_1, STRING_2 = ' '+input().rstrip(), ' '+input().rstrip()
STR_1_LEN, STR_2_LEN = len(STRING_1), len(STRING_2)
dp = [[0]*(STR_2_LEN) for _ in range(STR_1_LEN)]

# get and print LCS length.
for y in range(1, STR_1_LEN):
    for x in range(1, STR_2_LEN):
        dp[y][x] = dp[y-1][x-1]+1 if STRING_1[y] == STRING_2[x] else max(dp[y-1][x], dp[y][x-1])
print(dp[-1][-1])

if dp[-1][-1]: # if LCS exists, print LCS.
    y, x, LCS = STR_1_LEN-1, STR_2_LEN-1, ''
    while y >= 1 and x >= 1:
        if dp[y-1][x] == dp[y][x]:
            y -= 1
        elif dp[y][x-1] == dp[y][x]:
            x -= 1
        else:
            LCS += STRING_1[y]
            y -= 1
            x -= 1
    print(LCS[::-1])