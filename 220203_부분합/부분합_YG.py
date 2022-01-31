import sys

input = sys.stdin.readline

N, S = map(int, input().split())

arr = list(map(int, input().split()))

ans = 1e9

idx1 = 0
idx2 = 1

value = arr[idx1]
while 1:
    if value >= S:
        ans = min(ans, idx2-idx1)
        value -= arr[idx1]
        idx1 += 1

    else:
        if idx2 < N:
            value += arr[idx2]
            idx2 += 1

    if (idx2 == N and value < S) or idx1 == N:
        break


# 답 출력
if ans == 1e9:
    print(0)
else:
    print(ans)