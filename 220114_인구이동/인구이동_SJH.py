import sys
from collections import deque


def bfs(r, c, visit, nation):
    popluation = nation[r][c]
    count = 1
    queue = deque([(r, c)])
    visit[r][c] = True
    union = [(r, c)]

    while queue:
        r, c = queue.popleft()

        for nr, nc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr += r
            nc += c

            # 범위에서 벗어나는 경우나 이미 방문한 경우
            if not -1 < nr < N or not -1 < nc < N or visit[nr][nc]:
                continue
            
            # 인구 차이
            diff = abs(nation[r][c] - nation[nr][nc])

            # 연합이면
            if L <= diff <= R:
                queue.append((nr, nc))
                visit[nr][nc] = True
                popluation += nation[nr][nc]
                count += 1
                union.append((nr, nc))
    
    popluation //= count

    if count > 1:
        for r, c in union:
            nation[r][c] = popluation
        return True
    else:
        return False


input = sys.stdin.readline
N, L, R = map(int, input().split())
nation = [list(map(int, input().split())) for i in range(N)]

answer = 0
is_move = True

while is_move:
    visit = [[False for c in range(N)] for r in range(N)]

    for r in range(N):
        for c in range(N):
            if not visit[r][c]:
                is_move = is_move or bfs(r, c, visit, nation)
    
    if is_move:
        answer += 1

print(answer)