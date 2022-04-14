# https://www.acmicpc.net/problem/16948


from collections import deque


dxdy = [(-2, -1), (-2, +1), (0, -2), (0, +2), (+2, -1), (+2, +1)]

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[0] * N for _ in range(N)]


def bfs(r1, c1, r2, c2):
    q = deque([[(r1, c1), 0]])
    while q:
        node, cnt = q.popleft()
        if node == (r2, c2):
            return cnt
        x, y = node
        if visited[x][y]:
            continue
        visited[x][y] = 1

        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                q.append([(nx, ny), cnt + 1])
    return -1


print(bfs(r1, c1, r2, c2))
