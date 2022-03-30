# 벽, 바이러스 음수로 대체 → 바이러스 combination으로 구성 후 bfs로 최소 이동 시간 구하기
import sys, copy, collections, itertools
N, M = map(int, sys.stdin.readline().split())
MAPS = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

viruses = []
for r in range(N):
    for c in range(N):
        # wall replace: 1 → -1
        if MAPS[r][c] == 1:
            MAPS[r][c] = -1
        # virus replace: 2 → -2
        if MAPS[r][c] == 2:
            MAPS[r][c] = -2
            viruses.append((r, c))

def bfs(new_map, virus_locations):
    q = collections.deque()
    for r, c in virus_locations:
        new_map[r][c] = 1
        q.append((r, c, 1))

    while q:
        r, c, move = q.popleft()
        for nr, nc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = nr + r, nc + c
            if 0 <= nr < N and 0 <= nc < N:
                if new_map[nr][nc] == 0:
                    new_map[nr][nc] = move + 1
                    q.append((nr, nc, move + 1))
                elif new_map[nr][nc] == -2:
                    new_map[nr][nc] = 1
                    q.append((nr, nc, move + 1))

    cnt_zero = [new_map[r].count(0) for r in range(N)]
    if sum(cnt_zero) > 0:
        return -1
    else:
        return max(map(max, new_map)) - 1

result = 1e9
for candidate_viruses in itertools.combinations(viruses, M):
    move = bfs(copy.deepcopy(MAPS), candidate_viruses)
    if move != -1:
        result = min(result, move)

print(result) if result != 1e9 else print(-1)
