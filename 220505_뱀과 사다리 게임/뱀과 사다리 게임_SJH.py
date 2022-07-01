from collections import deque

n, m = map(int, input().split())
ladders = {}
snakes = {}

for _ in range(n):
    x, y = map(int, input().split())
    ladders[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    snakes[u] = v


can_visit = [True] * 101

queue = deque([(1, 0)])  # 현재 칸, 주사위 굴린 횟수
while queue:
    now, count = queue.popleft()
    if now == 100:
        print(count)
        break
    else:
        for dice in range(1, 7):
            nxt = now + dice

            if nxt in ladders:
                nxt = ladders[nxt]

            if nxt in snakes:
                nxt = snakes[nxt]

            if nxt < 101 and can_visit[nxt]:
                can_visit[nxt] = False
                queue.append((nxt, count+1))