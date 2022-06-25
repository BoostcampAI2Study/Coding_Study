import sys
def dfs(x, B):
    if x in SEQUENCE:
        if len(B) == N:
            print(' '.join(list(map(str, B))))
            sys.exit()
        if x % 3 == 0:
            dfs(x // 3, B + [x // 3])
        dfs(x * 2, B + [x * 2])

N = int(sys.stdin.readline())
SEQUENCE = list(map(int, sys.stdin.readline().split()))
for x in SEQUENCE:
    dfs(x, [x])
