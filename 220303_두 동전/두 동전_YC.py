from collections import deque

moves = [[1,0],[-1,0],[0,1],[0,-1]]
N, M = map(int, input().split())
visited = [[[[False]*(M+1) for _ in range(N+1)]for _ in range(M+1)] for _ in range(N+1)]
MAP = [list(input()) for _ in range(N)]

c1, c2 = [(n, m) for n in range(N) for m in range(M) if MAP[n][m] == 'o']

queue = deque()

answer = 11

queue.append((c1, c2, 0))

while queue:
    old_c1, old_c2, cnt = queue.popleft()
    for mx, my in moves:
        new_c1 = (old_c1[0]+mx, old_c1[1]+my) 
        new_c2 = (old_c2[0]+mx, old_c2[1]+my)
        if not visited[new_c1[0]][new_c1[1]][new_c2[0]][new_c2[1]]:
            visited[new_c1[0]][new_c1[1]][new_c2[0]][new_c2[1]]=True
            if not (0<=new_c1[0]<N and 0<=new_c1[1]<M) and not (0<=new_c2[0]<N and 0<=new_c2[1]<M):
                continue

            else:
                if (0<=new_c1[0]<N and 0<=new_c1[1]<M) and (0<=new_c2[0]<N and 0<=new_c2[1]<M):
                    if MAP[new_c1[0]][new_c1[1]] == '#': new_c1 = old_c1
                    if MAP[new_c2[0]][new_c2[1]] == '#': new_c2 = old_c2
                    queue.append((new_c1, new_c2, cnt+1))
                else:
                    answer = min(answer, cnt+1)
                    break
                
if answer == 11:
    print(-1)
else: print(answer)
