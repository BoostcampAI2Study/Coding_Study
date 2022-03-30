# 로봇 청소기 위치와 먼지 위치 찾기 → 각 위치간 거리 bfs로 계산 후 모두 저장 →
# 거리가 -1인 경우 먼지가 벽에 막혀 있는 것이므로 거리 계산 X → permutation으로 순서 정해줘서 최소 이동 거리 구하기
import sys, collections, itertools
while True:
    w, h = map(int, sys.stdin.readline().split())
    board = [sys.stdin.readline().strip() for _ in range(h)]

    if w == 0 and h == 0:
        break

    # 로봇 청소기 위치와 먼지 위치 찾기
    dirty_spaces = []
    for r in range(h):
        for c in range(w):
            if board[r][c] == 'o':
                dirty_spaces.insert(0, (r, c))
            if board[r][c] == '*':
                dirty_spaces.append((r, c))
    # 위치간 거리 계산
    def bfs(start_point, end_point):
        visit = [[False] * w for _ in range(h)]
        q = collections.deque()
        visit[start_point[0]][start_point[1]] = True
        q.append((start_point[0], start_point[1], 0))
        while q:
            r, c, move = q.popleft()
            if r == end_point[0] and c == end_point[1]:
                return move
            for nr, nc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = nr + r, nc + c
                if 0 <= nr < h and 0 <= nc < w and not visit[nr][nc] and board[nr][nc] != 'x':
                    visit[nr][nc] = True
                    q.append((nr, nc, move + 1))
        return -1

    # 각 거리간 bfs로 거리 계산한 값 저장
    distances = [[0] * len(dirty_spaces) for _ in range(len(dirty_spaces))]
    for i in range(len(dirty_spaces)):
        for j in range(i + 1, len(dirty_spaces)):
            distance = bfs(dirty_spaces[i], dirty_spaces[j])
            distances[i][j] = distance
            distances[j][i] = distance

    # 최소 이동 거리 구하기
    result = 1e9
    for candidate_list in itertools.permutations(range(1, len(dirty_spaces))):
        total_move = distances[0][candidate_list[0]]
        for i in range(1, len(candidate_list)):
            total_move += distances[candidate_list[i - 1]][candidate_list[i]]
        result = min(result, total_move)

    # 거리에 -1이 있는 경우 먼지가 벽에 막혀 있음
    if -1 in min(distances):
        print(-1)
    else:
        print(result)
