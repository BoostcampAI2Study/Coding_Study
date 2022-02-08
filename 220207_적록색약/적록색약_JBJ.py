import collections, sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline().strip())
RGB_BOARD = [sys.stdin.readline().strip() for _ in range(N)]
RB_BOARD = [[color if color != 'G' else 'R' for color in row] for row in RGB_BOARD]

rgb_visited, rgb_cnt = [[False] * N for _ in range(N)], 0
rb_visited, rb_cnt = [[False] * N for _ in range(N)], 0    # red==green

def grouping(y, x, color, is_rgb=True):
    global N, RGB_BOARD, RB_BOARD, rgb_board, rb_board
    if is_rgb:
        rgb_visited[y][x] = True
    else:
        rb_visited[y][x] = True

    for new_y, new_x in (y, x+1), (y, x-1), (y+1, x), (y-1, x):
        if 0 <= new_y < N and 0 <= new_x < N:
            if is_rgb and RGB_BOARD[new_y][new_x] == color and not rgb_visited[new_y][new_x]:
                grouping(new_y, new_x, color, True)
            elif not is_rgb and RB_BOARD[new_y][new_x] == color and not rb_visited[new_y][new_x]:
                grouping(new_y, new_x, color, False)       
                
for y in range(N):
    for x in range(N):
        if not rgb_visited[y][x]:
            grouping(y, x, RGB_BOARD[y][x], True)
            rgb_cnt += 1
        if not rb_visited[y][x]:
            grouping(y, x, RB_BOARD[y][x], False)
            rb_cnt += 1
            
print(rgb_cnt, rb_cnt)