# bfs → visit 배열에 이동 횟수 저장(K 개수 고려)
import sys, collections
K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())
MAPS = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

if W == 1 and H == 1:
    print(0)
    sys.exit()

visit = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
q = collections.deque()
q.append((0, 0, K, 0))
visit[0][0][K] = 1
while q:
    r, c, horse_cnt, move = q.popleft()
    if r == H - 1 and c == W - 1:
        continue
    if horse_cnt > 0:
        for nr, nc in [(-2, -1),(-1, -2),(-1, 2),(-2, 1),(2, -1),(1, -2),(1, 2),(2, 1)]:
            nr, nc = nr + r, nc + c
            if 0 <= nr < H and 0 <= nc < W and MAPS[nr][nc] != 1 and not visit[nr][nc][horse_cnt - 1]:
                visit[nr][nc][horse_cnt - 1] = move + 1
                q.append((nr, nc, horse_cnt - 1, move + 1))
    for nr, nc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = nr + r, nc + c
        if 0 <= nr < H and 0 <= nc < W and MAPS[nr][nc] != 1 and not visit[nr][nc][horse_cnt]:
            visit[nr][nc][horse_cnt] = move + 1
            q.append((nr, nc, horse_cnt, move + 1))

min_result = 1e9
for i in range(K + 1):
    if visit[H-1][W-1][i]:
        min_result = min(min_result, visit[H-1][W-1][i])
print(min_result) if min_result != 1e9 else print(-1)
