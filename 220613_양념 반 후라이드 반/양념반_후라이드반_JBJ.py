A, B, C, X, Y = map(int, input().split())
# seasoned_price, fried_price, fried_seasoned_price, seasoned_cnt, fried_cnt
 
if A + B < C * 2:
    print((A*X)+(B*Y))
else:
    M = min(X, Y)
    print((C*2*M) + (min(C*2, A) * max(0, X-M)) + (min(C*2, B) * max(0, Y-M)))