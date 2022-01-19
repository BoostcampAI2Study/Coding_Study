
def tetromino(i, j, m, mem, cnt, f=True, s=0):
    global answer         ## 이걸로 가지치기
    
    if answer >= s + 1000 * (4 - cnt):
        return
    if cnt == 4:
        answer = max(answer, s)
        return

    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ny, nx = i+dy, j+dx
        if 0 <= ny < len(m) and 0 <= nx < len(m[0]) and mem[ny][nx]:
            mem[ny][nx] = 0
            tetromino(ny, nx, m, mem, cnt+1, f, s+m[ny][nx])
            if f:
                tetromino(i, j, m, mem, cnt+1, False, s+m[ny][nx])
            mem[ny][nx] = 1

def solution(N, M):
    mem = [[1]*M for _ in range(N)]
    m = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        m.append(tmp)
    for i in range(N):
        for j in range(M):
            mem[i][j] = 0
            tetromino(i, j, m, mem, 1, True, m[i][j])
            mem[i][j] = 1

    return 0


N, M = list(map(int, input().split()))
answer = 0
solution(N, M)
print(answer)