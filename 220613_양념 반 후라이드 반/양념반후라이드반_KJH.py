A, B, C, X, Y = map(int, input().split())

cost = 0
if A + B > 2 * C:
    cost += min(X, Y) * 2 * C
    X, Y = X - min(X, Y), Y - min(X, Y)
if A > 2 * C:
    cost += X * 2 * C
    X, Y = 0, max(0, Y - X)
if B > 2 * C:
    cost += Y * 2 * C
    X, Y = max(0, X - Y), 0

cost += X * A + Y * B


print(cost)
