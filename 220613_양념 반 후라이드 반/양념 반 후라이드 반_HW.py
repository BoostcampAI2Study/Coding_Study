import sys
A, B, C, X, Y = map(int, sys.stdin.readline().split())
price = 0
if A + B < 2 * C:
    price = min(A, 2 * C) * X + min(B, 2 * C) * Y
else:
    chicken_cnt = min(X, Y)
    price = C * chicken_cnt * 2 + min(A, 2 * C) * (X - chicken_cnt) + min(B, 2 * C) * (Y - chicken_cnt)
print(price)
