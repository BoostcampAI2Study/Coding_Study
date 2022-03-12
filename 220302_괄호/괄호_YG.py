import sys
import math

input = sys.stdin.readline

def catalan(n):
    return math.factorial(2*n) // (math.factorial(n) * math.factorial(n+1))

T = int(input())

for _ in range(T):
    target = int(input())
    if target % 2 == 1:
        print(0)
    else:
        print(catalan(target // 2)% 1000000007)