from collections import deque
def solution(N, M, K):
    board = []
    mem = []
    for i in range(N):
        board.append(input())
        mem.append([99999999]*M)
    mem[0][0] = 1

    bfs = deque([(0, 0, K, 1)]) # y좌표, x좌표, 벽 부수기, 길이
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while bfs:
        y, x, k, d = bfs.popleft()
        for my, mx in move:
            ny, nx = y + my, x + mx
            if 0 <= ny < N and 0 <= nx < M and d+1 < mem[ny][nx]:
                if board[ny][nx] == '0':
                    bfs.append((ny, nx, k, d+1))
                    mem[ny][nx] = d+1
                elif board[ny][nx] == '1' and k:
                    bfs.append((ny, nx, k-1, d+1))
                    mem[ny][nx] = d+1
                if ny == N-1 and nx == M-1:
                    return d+1
                    

    return -1


N, M, K = list(map(int, input().split()))
print(solution(N, M, K))
