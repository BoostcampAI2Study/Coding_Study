from collections import deque
N, K = map(int, input().split(" "))

queue = deque([N])
time = [0]*100001

while queue:
    now = queue.popleft()
    if now == K:
        print(time[now])
        break
    for move in [now-1, now+1, 2*now]:
        if 0 <= move <= 100000:
            if not time[move]:
                time[move] = time[now] + 1
                queue.append(move)
