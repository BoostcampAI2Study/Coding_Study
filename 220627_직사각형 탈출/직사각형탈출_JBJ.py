import collections, sys

N, M = map(int, input().split())
BOARD = [list(map(int, input().split())) for _ in range(N)]
H, W, SR, SC, FR, FC = map(int, input().split())
SR, SC, FR, FC = SR-1, SC-1, FR-1, FC-1

WALLS = set()
for y in range(N):
    for x in range(M):
        if BOARD[y][x]: WALLS.add((y, x))

def contain_walls(y, x):
    global H, W, WALLS
    for wy, wx in WALLS:
        if y <= wy < y+H and x <= wx < x+W: return True
    return False

Q, visited = collections.deque([(SR, SC, 0)]), [[False]*(M-W+1) for _ in range(N-H+1)]
visited[SR][SC] = True
while Q:
    r, c, move_cnt = Q.popleft()

    if r == FR and c == FC: print(move_cnt); sys.exit()

    for new_r, new_c in (r, c+1), (r+1, c), (r-1, c), (r, c-1):
        if 0 <= new_r < (N-H+1) and 0 <= new_c < (M-W+1) and not visited[new_r][new_c]:
            visited[new_r][new_c] = True
            if not contain_walls(new_r, new_c):
                Q.append((new_r, new_c, move_cnt+1))
                
print(-1)