import sys
def get_cross(r, c):
    cross_size = 0
    for size in range(1, min(N, M)):
        is_cross = True
        for nr, nc in [(0, size), (0, -size), (size, 0), (-size, 0)]:
            nr, nc = r + nr, c + nc
            if 0 <= nr < N and 0 <= nc < M and BOARD[nr][nc] == '#' and not visit[nr][nc]:
                continue
            is_cross = False
            break
        if not is_cross:
            break
        cross_size += 1
    return cross_size

def visit_cross(r, c, size, is_visit):
    global visit
    visit[r][c] = is_visit
    for s in range(1, size + 1):
        for nr, nc in [(0, s), (0, -s), (s, 0), (-s, 0)]:
            nr, nc = r + nr, c + nc
            visit[nr][nc] = is_visit
            
N, M = map(int, sys.stdin.readline().split())
BOARD = [sys.stdin.readline().strip() for _ in range(N)]

result = 0
visit = [[False] * M for _ in range(N)]
for r in range(N):
    for c in range(M):
        if BOARD[r][c] == '#':
            cross_size = get_cross(r, c)
            for s in range(cross_size + 1):
                visit_cross(r, c, s, True)
                for cmpr_r in range(N):
                    for cmpr_c in range(M):
                        if BOARD[cmpr_r][cmpr_c] == '#':
                            cmpr_cross_size = get_cross(cmpr_r, cmpr_c)
                            result = max(result, (4 * s + 1) * (4 * cmpr_cross_size + 1))
                visit_cross(r, c, s, False)
print(result)
