from collections import deque

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, list(input()))))

moves = [[1,0],[0,1],[-1,0],[0,-1]]
visited = [[[False,False] for _ in range(M)] for _ in range(N)]

queue = deque([[0,0,1,True]])

answer = -1
while queue:
    r, c, cnt, break_wall = queue.popleft()
    if r == N-1 and c == M-1:
        answer = cnt
        break
    for mr, mc in moves:
        nr, nc = mr+r, mc+c
        if 0<= nr < N and 0<= nc < M:
            if not visited[nr][nc][break_wall]:
                visited[nr][nc][break_wall] = True
                if board[nr][nc] == 0:
                    queue.append([nr, nc, cnt+1, break_wall])
                elif board[nr][nc] == 1 and break_wall:
                    queue.append([nr, nc, cnt+1, False])

print(answer)
