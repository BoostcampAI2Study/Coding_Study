# bfs 사용
import sys, collections
N, M = map(int, sys.stdin.readline().split())
ladders = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
snakes = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

ladder_info, snake_info = collections.defaultdict(int), collections.defaultdict(int)
for ladder in ladders:
    idx1, idx2 = ladder
    ladder_info[idx1] = idx2
    ladder_info[idx2] = idx1

for snake in snakes:
    idx1, idx2 = snake
    snake_info[idx1] = idx2
    snake_info[idx2] = idx1

q = collections.deque()
q.append((1, 0))
visit = [False] * 101
result = 1e9
while q:
    cnt, move = q.popleft()
    if cnt == 100:
        result = move
        break

    for i in range(1, 7):
        next_space = cnt + i
        if next_space <= 100 and not visit[next_space]:
            visit[next_space] = True

            if ladder_info[next_space] and next_space < ladder_info[next_space]:
                q.append((ladder_info[next_space], move + 1))
                continue

            if snake_info[next_space] and next_space > snake_info[next_space]:
                q.append((snake_info[next_space], move + 1))
                continue

            q.append((next_space, move + 1))
print(result)
