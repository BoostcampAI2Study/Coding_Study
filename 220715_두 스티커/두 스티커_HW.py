import sys
def rotate(r, c):
    return c, r

def check(sticker1, sticker2):
    r1, c1 = sticker1
    r2, c2 = sticker2
    if (max(r1, r2) <= H and c1 + c2 <= W) or (max(c1, c2) <= W and r1 + r2 <= H):
        return True

H, W = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
STICKER_SIZES = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
      
result = 0
for i in range(N):
    r1, c1 = STICKER_SIZES[i][0], STICKER_SIZES[i][1]
    for j in range(i + 1, N):
        r2, c2 = STICKER_SIZES[j][0], STICKER_SIZES[j][1]
        if check([r1, c1], [r2, c2]) or check(rotate(r1, c1), [r2, c2]) or check([r1, c1], rotate(r2, c2)) or check(rotate(r1, c1), rotate(r2, c2)):
            result = max(result, r1 * c1 + r2 * c2)
print(result)
