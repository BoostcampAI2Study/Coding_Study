import sys, collections
N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# shark location
for r in range(N):
    for c in range(N):
        if board[r][c] == 9:
            board[r][c] = 0
            shark = [r, c]

# 가장 가까운 물고기 찾기
def bfs(shark, shark_size):
    visit = [[False] * N for _ in range(N)]
    q = collections.deque()
    candidate_fishes, min_move = [], 1e9

    q.append((shark[0], shark[1], 0))
    visit[shark[0]][shark[1]] = True

    while q:
        r, c, move = q.popleft()
        if 0 < board[r][c] < 7 and shark_size > board[r][c] and min_move >= move:
            min_move = move
            candidate_fishes.append([r, c, move]) # 가장 가까운 물고기 후보 저장
        if min_move < move:
            break

        for nr, nc in [(-1, 0), (0, -1),(1, 0), (0, 1)]:
            nr, nc = nr + r, nc + c
            if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc] and shark_size >= board[nr][nc]:
                visit[nr][nc] = True
                q.append((nr, nc, move + 1))

    if candidate_fishes:
        candidate_fishes.sort() # r, c 기반으로 sort해서 가장 가까운 물고기 앞쪽으로 보냄
        board[candidate_fishes[0][0]][candidate_fishes[0][1]] = 0 # 상어가 물고기 냠냠
        return candidate_fishes[0]
    return

move_cnt, eat_fish_cnt, shark_size = 0, 0, 2
while True:
    result = bfs(shark, shark_size)
    if result is None:
        print(move_cnt)
        break

    shark = [result[0], result[1]]  # shark r, c
    move_cnt += result[2]           # move
    eat_fish_cnt += 1

    if shark_size == eat_fish_cnt:
        shark_size += 1
        eat_fish_cnt = 0
