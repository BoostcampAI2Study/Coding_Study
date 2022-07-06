import sys
N = int(sys.stdin.readline())
ADDRESSES = [list(map(int, sys.stdin.readline().split('.'))) for _ in range(N)]

m = 0
is_break = False
for i in range(4):
    mask = 255
    for j in range(1, N):
        mask &= ~(ADDRESSES[j - 1][i] ^ ADDRESSES[j][i])
    for binary_num in bin(mask).replace('0b', ''):
        if binary_num == '0':
            is_break = True
            break
        else:
            m += 1
    if is_break:
        break

mask = '1' * m + '0' * (32-m)
network_mask, network_address = [0] * 4, [0] * 4
for i in range(4):
    network_mask[i] = str(int(mask[8 * i : 8 * (i + 1)], 2))
    address = bin(ADDRESSES[0][i]).replace('0b', '').zfill(8)
    cnt = mask[8 * i : 8 * (i + 1)].count('0')
    network_address[i] = str(int(address[:(8-cnt)] + '0' * cnt, 2))

print('.'.join(network_address))
print('.'.join(network_mask))
