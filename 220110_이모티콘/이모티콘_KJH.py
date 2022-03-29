from collections import defaultdict, deque


S = int(input())
visited = defaultdict(list)


def bfs():
    q = deque([(1, 0, 0)])  # display, clip, cnt
    while q:
        display, clip, cnt = q.popleft()
        if display == S:
            return cnt
        if display <= 0:
            continue
        if visited[display][clip]:
            continue
        visited[display].append(clip)
        for i in range(3):
            if i == 0 and clip != display:
                q.append((display, display, cnt + 1))
            elif i == 1:
                q.append((display + clip, clip, cnt + 1))
            elif i == 2:
                q.append((display - 1, clip, cnt + 1))


print(bfs())
