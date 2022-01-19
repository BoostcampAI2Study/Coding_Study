import sys

def dfs(tetromino, board, can_visit, max_sum):
    if len(tetromino) == 4:
        return sum([board[i][j] for i, j in tetromino])

    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    i, j = tetromino[-1]
    for m in move:
        ni = i + m[0]
        nj = j + m[1]
        
        if not -1 < ni < len(board) or not -1 < nj < len(board[0]):
            continue

        if (ni, nj) in tetromino:
            continue
        
        nxt_tet = tetromino[:] + [(ni, nj)]
        can_visit[ni][nj] = False
        max_sum = max(max_sum, dfs(nxt_tet, board, can_visit, max_sum))
    
    return max_sum


input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for n in range(N)]
can_visit = [[True for m in range(M)] for n in range(N)]
answer = 0

for i in range(N):
    for j in range(M):
        if can_visit[i][j]:
            can_visit[i][j] = False
            answer = max(answer, dfs([(i, j)], board, can_visit, board[i][j]))

print(answer)