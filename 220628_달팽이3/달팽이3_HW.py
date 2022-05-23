import sys
M, N = map(int, sys.stdin.readline().split())

cnt = (N - 1) * 2 + 1 if M > N else (M - 1) * 2
if M == N:
    r = M // 2 + 1 if M % 2 else M // 2 + 1
    c = r if N % 2 else N // 2
elif M > N:
    r = N // 2 + 1 + (M - N) if N % 2 else N // 2 + 1
    c = N // 2 + 1 if N % 2 else N // 2
else:
    r = M // 2 + 1 if M % 2 else M // 2 + 1
    c = M // 2 + 1 + (N - M) if M % 2 else M // 2

print(cnt)
print(r, c)
