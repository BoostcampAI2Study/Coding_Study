import sys, heapq

N, M = map(int, sys.stdin.readline().strip().split())
BOARD = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
max_weight_sum, MAX_WEIGHT = 0, max(map(max, BOARD))
visited = [[False]*M for _ in range(N)]

def dfs(y, x, square_cnt, weight_sum):
    global max_weight_sum, MAX_WEIGHT, N, M, BOARD, visited

    if max_weight_sum >= weight_sum + (MAX_WEIGHT * (4 - square_cnt)): return # backtracking

    if square_cnt == 4:
        max_weight_sum = max(max_weight_sum, weight_sum)
        return

    for new_y, new_x in ((y, x+1), (y, x-1), (y+1, x), (y-1, x)):
        if 0 <= new_y < N and 0 <= new_x < M and not visited[new_y][new_x]:
            if square_cnt == 2: # to make 'ㅗ, ㅜ' tetrominos.
                visited[new_y][new_x] = True
                dfs(y, x, square_cnt+1, weight_sum+BOARD[new_y][new_x])
                visited[new_y][new_x] = False
            visited[new_y][new_x] = True
            dfs(new_y, new_x, square_cnt+1, weight_sum+BOARD[new_y][new_x])
            visited[new_y][new_x] = False

for y in range(N):
    for x in range(M):
        visited[y][x] = True
        dfs(y, x, 1, BOARD[y][x])
        visited[y][x] = False

print(max_weight_sum)
