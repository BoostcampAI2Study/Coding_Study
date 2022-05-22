import sys, collections
N, M = map(int, sys.stdin.readline().split())
BOARD = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, sys.stdin.readline().split())

walls = []
for r in range(N):
    for c in range(M):
        if BOARD[r][c]:
            walls.append((r, c))

def check_walls(r, c):
    for w_r, w_c in walls:
        if r <= w_r < r + H and c <= w_c < c + W:
            return False
    return True

def bfs():
    NR = [0, 0, 1, -1]
    NC = [1, -1, 0, 0]
    q = collections.deque()
    q.append((Sr - 1, Sc - 1, 0))
    visit = [[False] * M for _ in range(N)]
    visit[Sr - 1][Sc - 1] = True

    while q:
        r, c, move = q.popleft()
        if r == Fr - 1 and c == Fc - 1:
            return move

        for i in range(4):
            nr, nc = r + NR[i], c + NC[i]
            if 0 <= nr < N and 0 <= nc < M and 0 <= nr + H - 1 < N and 0 <= nc + W - 1 < M and not visit[nr][nc] and check_walls(nr, nc):
                visit[nr][nc] = True
                q.append((nr, nc, move + 1))

    return -1
print(bfs())
