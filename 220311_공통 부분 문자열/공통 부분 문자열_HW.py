strings = [input() for _ in range(2)]
compare_strs = [[0] * (len(strings[1]) + 1) for _ in range(len(strings[0]) + 1)]

# compare strs
for idx1 in range(len(strings[0]) + 1):
    for idx2 in range(len(strings[1]) + 1):
        if idx1 == 0 or idx2 == 0:
            continue
        if strings[0][idx1 - 1] == strings[1][idx2 - 1]:
            compare_strs[idx1][idx2] = compare_strs[idx1 - 1][idx2 - 1] + 1

# max length
result = -1
for row in compare_strs:
    for num in row:
        if num > res:
            result = num
print(result)
