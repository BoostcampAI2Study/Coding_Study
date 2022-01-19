# (1, 1)이 좌상을 말하는건가 원점이 어디인지 말도 안해주네
# -- 시간초과...
from collections import deque

def bfs():
    cnt = 1
    q = deque([(0, 0, 0, 0)])
    visited = [(0, 0)]
    while q:
        cur_row, cur_col, is_break, cnt = q.popleft()
        
        if (cur_row, cur_col) == (N - 1, M - 1):
            return cnt + 1
        for d_row, d_col in move:
            nxt_row, nxt_col = cur_row + d_row, cur_col + d_col
            if 0 <= nxt_row < N and 0 <= nxt_col < M and (nxt_row, nxt_col) not in visited:
                if mat[nxt_row][nxt_col] == 1 and is_break < K:
                    q.append((nxt_row, nxt_col, is_break + 1, cnt + 1))
                if mat[nxt_row][nxt_col] == 0:
                    visited.append((nxt_row, nxt_col))
                    q.append((nxt_row, nxt_col, is_break, cnt + 1))
    return -1

if __name__ == '__main__':
    N, M, K = 6, 4, 2
    mat = [[0,1,0,0], [1,1,1,0], [1,0,0,0], [0,0,0,0], [0,1,1,1], [0,0,0,0]]
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    print(bfs())