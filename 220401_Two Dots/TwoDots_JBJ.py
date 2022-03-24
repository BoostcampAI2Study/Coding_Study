import collections, sys
sys.setrecursionlimit(10**7)
N, M = map(int, sys.stdin.readline().rstrip().split())
BOARD = [sys.stdin.readline().rstrip() for _ in range(N)]
visited = [[False]*M for _ in range(N)]

def dfs(y, x, prev_y, prev_x, color):
    global N, M, BOARD, visited
    visited[y][x] = True
    
    for new_y, new_x in (y, x+1), (y, x-1), (y+1, x), (y-1, x):
        if 0 <= new_y < N and 0 <= new_x < M and (new_y, new_x) != (prev_y, prev_x): # available board & skip previous y & x
            if BOARD[new_y][new_x] == color: # check color
                if visited[new_y][new_x]:
                    print('Yes')
                    sys.exit()
                dfs(new_y, new_x, y, x, color)
            
for y in range(N):
    for x in range(M):
        if not visited[y][x]:
            dfs(y, x, -1, -1, BOARD[y][x])
print('No')