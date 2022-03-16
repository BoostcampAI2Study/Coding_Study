import sys, collections, itertools, copy
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
max_safe_spaces = 0

def bfs(update_board, viruses_loc):
    global max_safe_spaces

    q = collections.deque()
    for virus in viruses_loc:
        q.append(virus)

    while q:
        r, c = q.popleft()
        for nr, nc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r + nr, c + nc
            if 0 <= nr < N and 0 <= nc < M and update_board[nr][nc] == 0:
                update_board[nr][nc] = 2
                q.append((nr, nc))

    cnt_zero = [update_board[i].count(0) for i in range(N)]
    max_safe_spaces = max(max_safe_spaces, sum(cnt_zero))

# 벽 3개 세울 수 있는 곳 + 바이러스 위치 찾기
wall_candidates = []
viruses = []
for r in range(N):
    for c in range(M):
        if board[r][c] == 0:
            wall_candidates.append((r, c))
        elif board[r][c] == 2:
            viruses.append((r, c))
# 벽 3개 + bfs
for three_walls in itertools.combinations(wall_candidates, 3):
    update_board = copy.deepcopy(board)
    for wall in three_walls:
        r, c = wall
        update_board[r][c] = 1
    bfs(update_board, viruses)

print(max_safe_spaces)
