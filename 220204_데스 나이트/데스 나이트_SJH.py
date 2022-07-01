from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

can_visit = [[True] * n for _ in range(n)]
queue = deque([(r1, c1, 0)])

while queue:
    r, c, move = queue.popleft()

    if (r, c) == (r2, c2):
        print(move)
        break
    else:
        for _r, _c in ((-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)):
            nr = r + _r
            nc = c + _c

            if -1 < nr < n and -1 < nc < n and can_visit[nr][nc]:
                can_visit[nr][nc] = False
                queue.append((nr, nc, move+1))
else:
    print(-1)