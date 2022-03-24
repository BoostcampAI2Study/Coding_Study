import sys, copy, collections, itertools
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
result = 1e9

# wall: 1 → '-', find viruses location
viruses = []
for r in range(N):
    for c in range(N):
        if board[r][c] == 1:
            board[r][c] = '-'
        elif board[r][c] == 2:
            viruses.append((r, c))

def bfs(new_board, viruses_loc):
    global result
    final_move = 0
    q = collections.deque()
    
    for virus in viruses_loc:
        q.append((virus[0], virus[1], 1))
        new_board[virus[0]][virus[1]] = 1

    while q:
        r, c, move = q.popleft()
        for nr, nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + nr, c + nc
            if 0 <= nr < N and 0 <= nc < N and new_board[nr][nc] == 0:
                new_board[nr][nc] = move + 1
                q.append((nr, nc, move + 1))

    cnt_zero = [new_board[r].count(0) for r in range(N)]
    if sum(cnt_zero) == 0:
        final_move = [new_board[r][c] for r in range(N) for c in range(N) if new_board[r][c] != '-']
        result = min(result, max(final_move))

for viruses_candidate in itertools.combinations(viruses, M):
    new_board = copy.deepcopy(board)
    for r in range(N):
        for c in range(N):
            if new_board[r][c] == 2 and (r, c) not in viruses_candidate:
                new_board[r][c] = 0
    bfs(new_board, viruses_candidate)

print(result - 1) if result != 1e9 else print(-1)
