from collections import defaultdict


xs, ys = map(int, input().split())
xe, ye = map(int, input().split())
graph = defaultdict(list)
for _ in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    graph[(x1, y1)].append((x2, y2))
    graph[(x2, y2)].append((x1, y1))
visited = set()

answer = float("inf")


def dfs(x, y, cnt):
    global visited, answer
    if (x, y) == (xe, ye):
        answer = min(answer, cnt)
        return
    dfs(xe, ye, cnt + abs(x - xe) + abs(y - ye))
    for tx, ty in graph.keys():
        tmp = abs(x - tx) + abs(y - ty)
        if (tx, ty) not in visited:
            visited.add((tx, ty))
            for nx, ny in graph[(tx, ty)]:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    dfs(nx, ny, cnt + tmp + 10)
                    visited.discard((nx, ny))
            visited.discard((tx, ty))


dfs(xs, ys, 0)
print(answer)
