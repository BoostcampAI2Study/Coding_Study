
def tetromino(i, j, m, mem, cnt, f=True, s=0):
    
    if cnt == 4:
        return s

    result = []
    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ny, nx = i+dy, j+dx
        if 0 <= ny < len(m) and 0 <= nx < len(m[0]) and mem[ny][nx]:
            mem[ny][nx] = 0
            result.append(tetromino(ny, nx, m, mem, cnt+1, f, s+m[ny][nx]))
            if f:
                result.append(tetromino(i, j, m, mem, cnt+1, False, s+m[ny][nx]))
            mem[ny][nx] = 1
    return max(result) if result else 0

def solution(N, M):
    answer = []
    mem = [[1]*M for _ in range(N)]
    m = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        m.append(tmp)
    for i in range(N):
        for j in range(M):
            mem[i][j] = 0
            answer.append(tetromino(i, j, m, mem, 1, True, m[i][j]))
            mem[i][j] = 1

    return max(answer)


N, M = list(map(int, input().split()))

print(solution(N, M))