import sys
N = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

cnt = 0
while True:
    is_div, is_empty = True, True
    for i in range(N):
        if B[i]:
            is_empty = False
        if B[i] % 2:
            cnt += 1
            B[i] -= 1
            is_div = False
    if is_empty:
        break
    if is_div:
        cnt += 1
        B = [B[i] // 2 for i in range(N)]
print(cnt)
