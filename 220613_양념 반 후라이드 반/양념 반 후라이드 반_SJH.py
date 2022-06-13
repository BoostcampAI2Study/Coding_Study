a, b, c, x, y = map(int, input().split())

both_min = min(a+b, c+c)
common = min(x, y)
price1 = both_min * common + a * (x-common) + b * (y-common)
price2 = both_min * max(x, y)

print(min(price1, price2))
