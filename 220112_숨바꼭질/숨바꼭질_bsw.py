from collections import deque

N, K = map(int, input().split())

q=deque([N])
visited = {N:0}

while q:
    cur = q.popleft()
    
    if cur == K:
        print(visited[cur])
        break

    for next in cur-1, cur+1, cur*2:
        if next in visited:
            continue

        if 0<=next<=100000:
            q.append(next)
            visited[next] = visited[cur] + 1
