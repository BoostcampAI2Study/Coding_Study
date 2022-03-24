from collections import deque
import sys
import copy
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

tx, ty = -1, -1
bx, by = -1, -1
rx, ry = -1, -1
for x in range(N):
    for y in range(M):
        if board[x][y] == 'B':
            bx, by = x, y
        elif board[x][y] == 'R':
            rx, ry = x, y
        elif board[x][y] == 'O':
            tx, ty = x, y

# 상, 하, 좌, 우
dx = [0,1,0,-1]
dy = [1,0,-1,0]

q = deque()

q.append((0, rx, ry, bx, by))

visited = set()
visited.add((rx, ry, bx, by))

while q:
    level, r_x, r_y, b_x, b_y = q.popleft()

    # 10번만에 못빼면 -1 출력
    if level > 10:
        continue

    # 답 출력
    if board[r_x][r_y] == 'O':
        print(level)
        break

    # 조건에 맞게 이동
    for k in range(4):
        r_move = 0
        b_move = 0

        # r 움직이기
        nrx = r_x + dx[k]
        nry = r_y + dy[k]

        while 1:
            if board[nrx][nry] == '#':
                nrx -= dx[k]
                nry -= dy[k]
                break
            elif board[nrx][nry] == 'O':
                break
            nrx += dx[k]
            nry += dy[k]

            r_move += 1

        # b 움직이기
        nbx = b_x + dx[k]
        nby = b_y + dy[k]
        while 1:
            if board[nbx][nby] == '#':
                nbx -= dx[k]
                nby -= dy[k]
                break
            elif board[nbx][nby] == 'O':
                break
            nbx += dx[k]
            nby += dy[k]
            b_move += 1

        # B는 빠지면 X
        if board[nbx][nby] == 'O':
            continue

        # R, B 같은 경우 제외
        if nrx == nbx and nry == nby:
            if r_move > b_move:
                nrx -= dx[k]
                nry -= dy[k]
            else:
                nbx -= dx[k]
                nby -= dy[k]

        if not (nrx, nry, nbx, nby) in visited:
            visited.add((nrx, nry, nbx, nby))
            q.append((level+1, nrx, nry, nbx, nby))

else:
    print(-1)
