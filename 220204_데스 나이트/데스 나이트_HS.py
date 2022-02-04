N = int(input())
r1, c1, r2, c2 = list(map(int, input().split()))

# Memoization
visited = [[0] * N for _ in range(N)]
visited[r1][c1] = 1
# Moving radius
move = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
# Using bfs
bfs = [(r1, c1, 0)]
for r, c, d in bfs:
    # When the horse arrives at the target, break
    if r == r2 and c == c2:
        print(d)
        break
    for mr, mc in move:
        nr, nc = r + mr, c + mc
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
            bfs.append((nr, nc, d+1))
            visited[nr][nc] = 1
# if break didn't happen
else:
    print(-1)