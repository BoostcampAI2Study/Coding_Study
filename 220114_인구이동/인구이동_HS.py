N, L, R = map(int, input().split())

m = []
for i in range(N):
    tmp = list(map(int, input().split()))
    m.append(tmp)

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer = 0

mem = []
while True:
    mem.clear()
    n_of_unions = 0
    for c in range(N):
        for r in range(N):
            if (c, r) not in mem:
                s = m[c][r]
                mem.append((c, r))
                union = [(c, r)]
                n_of_unions += 1
                for y, x in union:
                    for my, mx in move:
                        ny, nx = y + my, x + mx
                        if (ny, nx) not in mem and 0 <= ny < N and 0 <= nx < N:
                            if L <= abs(m[y][x] - m[ny][nx]) <= R:
                                s += m[ny][nx]
                                union.append((ny, nx))
                                mem.append((ny, nx))
                for y, x in union:
                    m[y][x] = s//len(union)
    if n_of_unions == N*N:
        break
    answer += 1

print(answer)