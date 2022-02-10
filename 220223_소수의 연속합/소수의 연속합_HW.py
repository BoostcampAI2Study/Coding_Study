import sys
N = int(input())
prime_check = [True] * (N + 1)
prime_list = []

# N이 1이면 print 0
if N == 1:
    print(0)
    sys.exit()

# 소수 확인
prime_check[1] = False   # 1 is not prime number
m = int(N ** 0.5)
for num in range(2, m + 1):
    if prime_check[num]:
        for i in range(2 * num, N + 1, num):
            prime_check[i] = False

# 소수 리스트 생성
for num in range(N):
    if prime_check[num + 1]:
        prime_list.append(num + 1)

# 소수 합 count
left, right = 0, 0
total, cnt = prime_list[left], 0
while left <= right:
    if total == N:
        cnt += 1
    if total < N:
        right += 1
        if right >= len(prime_list):
            break
        total += prime_list[right]
        continue
    total -= prime_list[left]
    left += 1
print(cnt)