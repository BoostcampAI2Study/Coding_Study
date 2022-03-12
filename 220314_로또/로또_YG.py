import sys

input = sys.stdin.readline

while 1:
    arr = list(map(int, input().split()))

    if arr[0] == 0:
        break

    num, lotto = arr[0], arr[1:]

    def dfs(level, answer, mark):
        if level == 6:
            print(" ".join(map(str,answer)))

        for value in range(mark, num):
            dfs(level+1, answer+[lotto[value]], value+1)


    dfs(0, [], 0)
    print()
