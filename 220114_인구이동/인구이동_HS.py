N, L, R = map(int, input().split())

m = []
for i in range(N):
    tmp = list(map(int, input().split()))
    m.append(tmp)

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer = 0

while True:
    mem = [[1] * N for _ in range(N)]
    n_of_unions = 0
    for c in range(N):
        for r in range(N):
            if mem[c][r]:
                s = m[c][r]
                mem[c][r] = 0
                union = [(c, r)]
                n_of_unions += 1
                for y, x in union:
                    for my, mx in move:
                        ny, nx = y + my, x + mx
                        if 0 <= ny < N and 0 <= nx < N and mem[ny][nx]:
                            if L <= abs(m[y][x] - m[ny][nx]) <= R:
                                s += m[ny][nx]
                                union.append((ny, nx))
                                mem[ny][nx] = 0
                for y, x in union:
                    m[y][x] = s//len(union)
    if n_of_unions == N*N:
        break
    answer += 1

print(answer)