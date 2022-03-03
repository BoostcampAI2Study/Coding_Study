# 풀이보고 풀었음 (카탈란 수열 사용)

from math import factorial
NUM = 1000000007
T = int(input())

for _ in range(T):
    L = int(input())
    if L % 2:
        print(0)
    else:
        n = L//2
        print(factorial(2*n)//(factorial(n+1)*factorial(n))%NUM)
