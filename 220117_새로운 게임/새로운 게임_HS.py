def check(y, x, m, N):
    if 0 <= y < N and 0<= x < N:
        return m[y][x]
    return -1

N, K = map(int, input().split())
m = []
m2 = [['-1'] * N for _ in range(N)]
horses = dict()
move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
answer = 0

for i in range(N):
    tmp = list(map(int, input().split()))
    m.append(tmp)

for i in range(K):
    r, c, v = list(map(int, input().split()))
    m2[r-1][c-1] = str(i)
    horses[str(i)] = {'coor': (r-1, c-1), 'dir': v}

for i in range(K*1001):
    n = str(i % K)
    r, c = horses[n]['coor']
    v = horses[n]['dir']

    if int(n) == 0:
        answer += 1
    if answer > 1000:
        break

    if m2[r][c][0] == n:
        my, mx = move[v-1]
        ny, nx = r + my, c + mx


        color = check(ny, nx, m, N)

        if color == 0:
            m2[ny][nx] = m2[r][c] if m2[ny][nx] == '-1' else m2[ny][nx] + m2[r][c] # 문자열 더하기 (extend)
            for _n in m2[r][c]:
                horses[_n]['coor'] = (ny, nx)       # 좌표 갱신
            m2[r][c] = '-1'                         # 옮겼으니까 빈 곳 처리
        elif color == 1:
            m2[ny][nx] = m2[r][c][::-1] if m2[ny][nx] == '-1' else m2[ny][nx] + m2[r][c][::-1] # 문자열 더하기 (extend)
            for _n in m2[r][c]:
                horses[_n]['coor'] = (ny, nx)
            m2[r][c] = '-1'
        elif color in [2, -1]:
            ny, nx = r - my, c - mx
            v += -1 + (v%2) * 2
            if check(ny, nx, m, N) in [2, -1]:
                horses[n]['dir'] = v
            else:
                if check(ny, nx, m, N):
                    m2[ny][nx] = m2[r][c][::-1] if m2[ny][nx] == '-1' else m2[ny][nx] + m2[r][c][::-1] # 문자열 더하기 (extend)
                else:
                    m2[ny][nx] = m2[r][c] if m2[ny][nx] == '-1' else m2[ny][nx] + m2[r][c] # 문자열 더하기 (extend)
                for _n in m2[r][c]:
                    horses[_n]['coor'] = (ny, nx)
                horses[n]['dir'] = v
                m2[r][c] = '-1'

        if check(ny, nx, m, N) != -1 and len(m2[ny][nx]) >= 4:
            break

if answer > 1000:
    print(-1)
else:
    print(answer)


