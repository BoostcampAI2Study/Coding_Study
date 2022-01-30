import sys
sys.setrecursionlimit(10**5)

"""
c\a\b\c\
 b\c\a\b\
  a\b\c\a\
   b\a\c\b\... 
"""
N = int(sys.stdin.readline().strip())
BOARD = [sys.stdin.readline().strip() for _ in range(N)]
DY = [-1, -1, 0, 1, 1, 0]
DX = [0, 1, 1, 0, -1, -1]
"""
 \0\1     \a\b
 5\*\2    b\*\a
  4\3\     a\b\
"""

color_board, min_colors = [[0] * N for _ in range(N)], 0
def dfs(y, x):
    global color_board, min_colors
    min_colors = max(min_colors, color_board[y][x]) # 1 or 2

    # nearby spaces check
    for idx in range(6):
        new_y, new_x = y + DY[idx], x + DX[idx]
        if 0 <= new_y < N and 0 <= new_x < N and BOARD[new_y][new_x] == 'X':
            if color_board[new_y][new_x] == 0: # colorless space
                color_board[new_y][new_x] = 3-color_board[y][x] # coloring 1 or 2
                dfs(new_y, new_x)
            if color_board[new_y][new_x] == color_board[y][x]: # colored space
                min_colors = max(min_colors, 3) # need to color 3

for y in range(N):
    for x in range(N):
        if BOARD[y][x] == 'X' and not color_board[y][x]:
            color_board[y][x] = 1
            dfs(y, x)

print(min_colors)