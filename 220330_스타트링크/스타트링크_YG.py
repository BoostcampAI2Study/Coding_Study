import sys
from collections import deque
input = sys.stdin.readline

# F: 총 층수, S: 강호 위치, G: 스타트링크 위치, U: 위로, D: 아래로
F, S, G, U, D = map(int, input().split())

# 방문 체크
visited = [False]*(F+1)

# bfs
q = deque()
q.append((S, 0))
visited[S] = True
while q:
    where, cnt = q.popleft()
    if where == G:
        print(cnt)
        break

    for next_where in [where+U, where-D]:
        if 1 <= next_where <= F and visited[next_where] == False:
            visited[next_where] = True
            q.append((next_where, cnt+1))

else:
    print("use the stairs")


