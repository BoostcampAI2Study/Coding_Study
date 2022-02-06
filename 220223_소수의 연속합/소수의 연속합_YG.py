import sys

input = sys.stdin.readline

N = int(input())

ans = 0

# 에라토스테네스의 체
arr = [True] * (N+1)
arr[0] = False
arr[1] = False

prime_list = []
for i in range(2, N+1):
    if arr[i] == True:
        prime_list.append(i)
        for j in range(2*i, N+1, i):
            arr[j] = False

idx1 = 0
idx2 = 1

if not prime_list:
    print(0)
    sys.exit()

value = prime_list[0]
while 1:

    if value == N:
        ans += 1
        if idx2 < len(prime_list):
            value -= prime_list[idx1]
            value += prime_list[idx2]
        idx1 += 1
        idx2 += 1

    elif value < N:
        if idx2 < len(prime_list):
            value += prime_list[idx2]
        idx2 += 1
    else:
        value -= prime_list[idx1]
        idx1 += 1

    if idx2 == len(prime_list)+1:
        break

print(ans)