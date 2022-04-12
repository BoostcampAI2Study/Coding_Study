import collections, sys

K = int(sys.stdin.readline().rstrip())
W, H = map(int, sys.stdin.readline().rstrip().split())
BOARD = [list(map(lambda x: -1 if x == '0' else -2, sys.stdin.readline().rstrip().split())) for _ in range(H)] # -1: space, -2: hurdle

def bfs():
    global K, W, H, BOARD

    BOARD[0][0] = K
    Q = collections.deque([(0, 0, 0, K)]) # y, x, move_cnt, k_left_cnt
    while Q:
        y, x, move_cnt, k_left_cnt = Q.popleft()

        if (y, x) == (H-1, W-1): return move_cnt
        
        # monkey moves
        for new_y, new_x in (y+1, x), (y-1, x), (y, x+1), (y, x-1):
            if 0 <= new_y < H and 0 <= new_x < W and BOARD[new_y][new_x] != -2 and BOARD[new_y][new_x] < k_left_cnt:
                if (new_y, new_x) == (H-1, W-1): return move_cnt+1
                BOARD[new_y][new_x] = k_left_cnt
                Q.append((new_y, new_x, move_cnt+1, k_left_cnt))
        
        # horse moves
        if k_left_cnt > 0:
            for new_y, new_x in (y+2, x-1), (y+2, x+1), (y-2, x-1), (y-2, x+1), (y+1, x-2), (y-1, x-2), (y+1, x+2), (y-1, x+2):
                if 0 <= new_y < H and 0 <= new_x < W and BOARD[new_y][new_x] != -2 and BOARD[new_y][new_x] < k_left_cnt-1:
                    if (new_y, new_x) == (H-1, W-1): return move_cnt+1
                    BOARD[new_y][new_x] = k_left_cnt-1
                    Q.append((new_y, new_x, move_cnt+1, k_left_cnt-1))
    return -1

print(bfs())