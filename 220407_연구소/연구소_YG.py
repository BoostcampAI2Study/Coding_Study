from itertools import combinations
from collections import deque
import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

blank_list = []
for x in range(N):
    for y in range(M):
        if board[x][y] == 0:
            blank_list.append((x, y))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def virus(board, x, y, visited):

    q = deque()

    q.append((x, y))

    while q:
        nx, ny = q.popleft()

        for k in range(4):
            nnx, nny = nx+dx[k], ny+dy[k]
            if 0 <= nnx < N and 0 <= nny < M and visited[nnx][nny] == False and board[nnx][nny] == 0:
                visited[nnx][nny] = True
                board[nnx][nny] = 2
                q.append((nnx, nny))

    return board, visited


answer = 0
for fence in list(combinations(blank_list, 3)):

    copy_board = copy.deepcopy(board)
    # 벽 세우기
    for a, b in fence:
        copy_board[a][b] = 1

    visited = [[False]*M for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if copy_board[x][y] == 2:
                visited[x][y] = True
                copy_board, visited = virus(copy_board, x, y, visited)


    answer = max(answer, sum(map(lambda x: x.count(0), copy_board)))

print(answer)