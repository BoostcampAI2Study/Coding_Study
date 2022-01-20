from collections import deque
def solution(N, M, K):
    answer = []
    board = []
    mem = [[[1] * M for _ in range(N)] for __ in range(K+1)]
    for i in range(N):
        board.append(input())
    mem[K][0][0] = 0

    bfs = deque([(0, 0, K, 1)]) # y좌표, x좌표, 벽 부수기, 길이
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while bfs:
        y, x, k, d = bfs.popleft()
        if y == N-1 and x == M-1:
            answer.append(d)
            continue
        for my, mx in move:
            ny, nx = y + my, x + mx
            if 0 <= ny < N and 0 <= nx < M and mem[k][ny][nx]:
                if board[ny][nx] == '0':
                    bfs.append((ny, nx, k, d+1))
                    mem[k][ny][nx] = 0
                elif board[ny][nx] == '1' and k:
                    bfs.append((ny, nx, k-1, d+1))
                    mem[k-1][ny][nx] = 0            
    if answer:
        return min(answer)
    return -1


N, M, K = list(map(int, input().split()))
if N==1 and M==1 and K==1:
    input()
    print(1)
else:
    print(solution(N, M, K))
