import sys

def dfs(tetromino, board, length=0, max_sum = 0):
    if length == 4:
        return sum([board[i][j] for i, j in tetromino])

    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    i, j = tetromino[-1]
    for m in move:
        ni = i + m[0]
        nj = j + m[1]

        if not -1 < ni < len(board) or not -1 < ni < len(board[0]):
            continue

        if (ni, nj) in tetromino:
            continue
        
        nxt_tet = tetromino[:] + [(ni, nj)]
        length += 1

        return max(max_sum, dfs(nxt_tet, board, length, max_sum))
    
    return 0


input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for n in range(N)]
answer = 0

for i in range(N):
    for j in range(M):
        answer = max(answer, dfs([(i, j)], board))

print(answer)