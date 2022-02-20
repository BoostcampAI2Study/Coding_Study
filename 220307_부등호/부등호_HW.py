k = int(input())
signs = input().split()

result = []
def dfs(idx, select_nums):
    global result
    if len(select_nums) == k + 1:
        result.append(select_nums)
        return

    sign, cmpr_num = signs[idx], int(select_nums[idx])
    for num in range(10):
        if str(num) in select_nums:
            continue
        if sign == "<":
            if cmpr_num < num:
                dfs(idx + 1, select_nums + str(num))
        else:
            if cmpr_num > num:
                dfs(idx + 1, select_nums + str(num))

for i in range(10):
    dfs(0, str(i))

print(result[-1])
print(result[0])
