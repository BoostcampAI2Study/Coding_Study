import collections, sys
N = int(sys.stdin.readline().strip())
R1, C1, R2, C2 = map(int, sys.stdin.readline().strip().split())

def bfs():
    global N, R1, C1, R2, C2
    board = [[-1] * N for _ in range(N)]

    Q = collections.deque()
    Q.append((R1, C1, 0))

    while Q:
        r, c, move_cnt = Q.popleft()

        if (r, c) == (R2, C2):
            return move_cnt

        for new_r, new_c in  (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1):
            if 0 <= new_r < N and 0 <= new_c < N and board[new_r][new_c] == -1:
                board[new_r][new_c] = move_cnt+1
                Q.append((new_r, new_c, move_cnt+1))
    return -1
    
print(bfs())     