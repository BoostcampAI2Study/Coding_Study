M, N = map(int, input().split())

print((M-1)*2 if N >= M else (N-1)*2+1)

if M == N:
    print(f'{M//2+1} {N//2+1}' if M%2 else f'{M//2+1} {N//2}')
elif M > N:
    print(f'{N//2+1} {N//2}' if N%2 == 0 else f'{N//2+1+(M-N)} {N//2+1}')
else:
    print(f'{M//2+1} {M//2}' if M%2 == 0 else f'{M//2+1} {M//2+1+(N-M)}')
