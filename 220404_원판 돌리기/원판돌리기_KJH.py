# https://www.acmicpc.net/problem/17822

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, T = map(int, input().split())

circles = [list(map(int, input().split())) for _ in range(N)]

zero_cnt = 0


def dfs(node, num, update=False):
    global zero_cnt
    x, y = node
    circles[x][y] = 0
    zero_cnt += 1
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N:
            if ny < 0:
                ny += M
            elif ny >= M:
                ny -= M
            if circles[nx][ny] == num:
                update = True
                dfs((nx, ny), num, update)
    return update


for _ in range(T):
    x, d, k = map(int, input().split())
    for i in range(x, len(circles) + 1, x):
        i -= 1
        if d:
            circles[i] = circles[i][k:] + circles[i][:k]
        else:
            circles[i] = circles[i][-k:] + circles[i][:-k]
    update = False
    for i in range(N):
        for j in range(M):
            if circles[i][j] != 0:
                num = circles[i][j]
                if not dfs((i, j), num):
                    circles[i][j] = num
                    zero_cnt -= 1
                else:
                    update = True

    if zero_cnt == N * M:
        print(0)
        sys.exit()
    elif not update:
        tmp = 0
        tmp = sum(map(sum, circles)) / (N * M - zero_cnt)
        for i in range(N):
            for j in range(M):
                if circles[i][j]:
                    if circles[i][j] > tmp:
                        circles[i][j] -= 1
                    elif circles[i][j] < tmp:
                        circles[i][j] += 1

print(sum(map(sum, circles)))
