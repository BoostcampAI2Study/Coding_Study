from collections import deque, defaultdict
import sys

input = sys.stdin.readline

stones = list(map(int, input().split()))

stones.sort()

q = deque()

q.append(stones)

visited = defaultdict(bool)

visited[tuple(stones)] = True

while q:
    a, b, c = q.popleft()

    if a==b==c:
        print(1)
        sys.exit()

    # a, b
    if a==b or 2*a == b:
        pass
    else:
        next_stones = sorted([2*a, b-a, c])
        if visited[tuple(next_stones)] == False:
            visited[tuple(next_stones)] = True
            q.append(next_stones)

    # b, c
    if b==c or 2*b == c:
        pass
    else:
        next_stones = sorted([a, 2*b, c-b])
        if visited[tuple(next_stones)] == False:
            visited[tuple(next_stones)] = True
            q.append(next_stones)

    # a, c
    if c==a or 2*a == c:
        pass
    else:
        next_stones = sorted([2*a, b, c-a])
        if visited[tuple(next_stones)] == False:
            visited[tuple(next_stones)] = True
            q.append(next_stones)
print(0)