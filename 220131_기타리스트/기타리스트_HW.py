N, S, M = map(int, input().split())
V = list(map(int, input().split()))

result = -1
check = [[False]*(M+1) for _ in range(N)]

def cal_volume(volume, idx):
    global result
    if idx == N:
        if result < volume:
            result = volume
        return
    if check[idx][volume] is False:
        max_v, min_v = volume + V[idx], volume - V[idx]
        check[idx][volume] = True
    else:
        return
    if max_v <= M:
        cal_volume(max_v, idx + 1)
    if min_v >= 0:
        cal_volume(min_v, idx + 1)

cal_volume(S, 0)
print(result)