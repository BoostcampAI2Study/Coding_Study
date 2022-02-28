from collections import deque

moves = {0:[0,1], 1:[0,-1], 2:[1,0], 3:[-1,0]}

W, H = map(int, input().split())

MAP = [list(input()) for _ in range(H)]
visited = [[float('inf')]*(W) for _ in range(H)]

c1, c2 = [(h,w) for h in range(H) for w in range(W) if MAP[h][w]=='C']

queue = deque()

queue.append((c1, -1, -1))

visited[c1[0]][c1[1]] = -1

while queue:
    (row, col), drt, cnt = queue.popleft()
        
    for new_d, (mr, mc) in moves.items():
        new_r, new_c = row+mr, col+mc
        if 0<=new_r<H and 0<=new_c<W and MAP[new_r][new_c] != '*':
            if new_d == drt:
                if visited[new_r][new_c] >= cnt:
                    visited[new_r][new_c] = cnt
                    queue.append(((new_r, new_c), new_d, cnt))
            else:
                if visited[new_r][new_c] >= cnt+1:
                    visited[new_r][new_c] = cnt+1
                    queue.append(((new_r, new_c), new_d, cnt+1))

print(visited[c2[0]][c2[1]])
