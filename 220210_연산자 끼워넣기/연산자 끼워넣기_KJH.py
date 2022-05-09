# https://www.acmicpc.net/problem/14888

N = int(input())
A_list = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_num = -float("inf")
min_num = float("inf")


def dfs(sums, pl, mi, mu, di, cnt):
    global min_num, max_num
    if cnt == N:
        min_num = min(min_num, sums)
        max_num = max(max_num, sums)
        return

    if pl:
        dfs(sums + A_list[cnt], pl - 1, mi, mu, di, cnt + 1)
    if mi:
        dfs(sums - A_list[cnt], pl, mi - 1, mu, di, cnt + 1)
    if mu:
        dfs(sums * A_list[cnt], pl, mi, mu - 1, di, cnt + 1)
    if di:
        if sums < 0:
            tmp = -sums // A_list[cnt]
            dfs(-tmp, pl, mi, mu, di - 1, cnt + 1)
        else:
            dfs(sums // A_list[cnt], pl, mi, mu, di - 1, cnt + 1)


dfs(A_list[0], plus, minus, mul, div, 1)

print(max_num)
print(min_num)
