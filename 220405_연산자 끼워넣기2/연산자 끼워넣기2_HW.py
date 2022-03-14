import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
operator_cnt = list(map(int, sys.stdin.readline().split()))

max_res, min_res = -1e9, 1e9

def dfs(idx, operator_list, cal_res):
    global min_res, max_res
    if idx == N - 1:
        min_res = min(min_res, cal_res)
        max_res = max(max_res, cal_res)
        return

    add, sub, mul, div = operator_list
    if operator_list[0] > 0:
        dfs(idx + 1, [add - 1, sub, mul, div], cal_res + A[idx + 1])
    if operator_list[1] > 0:
        dfs(idx + 1, [add, sub - 1, mul, div], cal_res - A[idx + 1])
    if operator_list[2] > 0:
        dfs(idx + 1, [add, sub, mul - 1, div], cal_res * A[idx + 1])
    if operator_list[3] > 0:
        if cal_res < 0:
            dfs(idx + 1, [add , sub, mul, div - 1], -(abs(cal_res) // A[idx + 1]))
        else:
            dfs(idx + 1, [add , sub, mul, div - 1], cal_res // A[idx + 1])

dfs(0, operator_cnt, A[0])
print(max_res)
print(min_res)
