from collections import deque
def solution(N, M, K):
    board = []
    mem = [[[1] * M for _ in range(N)] for __ in range(K)]
    for i in range(N):
        board.append(input())
    mem[K-1][0][0] = 1

    bfs = deque([(0, 0, K, 1)]) # y좌표, x좌표, 벽 부수기, 길이
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while bfs:
        y, x, k, d = bfs.popleft()
        for my, mx in move:
            ny, nx = y + my, x + mx
            if 0 <= ny < N and 0 <= nx < M and mem[k-1][ny][nx]:
                if board[ny][nx] == '0':
                    bfs.append((ny, nx, k, d+1))
                    mem[k-1][ny][nx] = 0
                elif board[ny][nx] == '1' and k:
                    bfs.append((ny, nx, k-1, d+1))
                    mem[k-2][ny][nx] = 0
                if ny == N-1 and nx == M-1:
                    return d+1                   

    return -1


N, M, K = list(map(int, input().split()))
print(solution(N, M, K))
