'''
https://www.acmicpc.net/problem/5014
BFS로 풀었다
'''
from sys import stdin
from collections import deque

input = stdin.readline
f, s, g, u, d = map(int, input().split())

can_visit = [True for _ in range(f+1)]
queue = deque([(s, 0)]) # 이전 방문 층, 버튼 누른 횟수
can_visit[s] = False

while queue:
    now, count = queue.popleft()

    # 내려야하는 층 도착했으면
    if now == g:
        print(count)
        break
    
    # 도착하지 않았으면
    # 방문하지 않은 층이면 올라가는 버튼 누르기
    nxt = now + u
    if nxt <= f and can_visit[nxt]:
        queue.append((nxt, count+1))
        can_visit[nxt] = False

    # 방문하지 않은 층이면 내려가는 버튼 누르기
    nxt = now - d
    if nxt > 0 and can_visit[nxt]:
        queue.append((nxt, count+1))
        can_visit[nxt] = False

else:
    print('use the stairs')