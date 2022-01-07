from collections import deque

# 수빈이가 있는 위치 N, 동생이 있는 위치 K
N, K = map(int, input().split())

# 좌표별로 최단시간구하기
dots = [1e9]*100001
dots[N] = 0

# N부터 BFS 진행
q = deque()
q.append((N, 0))

while q:
    now, time = q.popleft()
    # 뒤로
    future = now-1
    if 0 <= future <= 100000 and dots[future] > time+1:
        dots[future] = time+1
        q.append((future, time+1))

    # 앞으로
    future = now+1
    if 0 <= future <= 100000 and dots[future] > time+1:
        dots[future] = time+1
        q.append((future, time+1))

    # 순간이동
    future = now*2
    if 0 <= future <= 100000 and dots[future] > time+1:
        dots[future] = time+1
        q.append((future, time+1))

print(dots[K])
