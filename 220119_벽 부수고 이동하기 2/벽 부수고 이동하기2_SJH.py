from collections import deque
import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
board = [[int(i) for i in input().rstrip('\n')] for n in range(N)]
visit = [[0 for m in range(M)] for n in range(N)]
visit[0][0] = 1
queue = deque([[0, 0, 0]]) # 행, 열, 벽 부순 수

while queue:
    i, j, k = queue.popleft()

    for _i, _j  in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni = i + _i
        nj = j + _j

        if not -1 < ni < N or not -1 < nj < M or visit[ni][nj] > 0:
            continue
        
        if board[ni][nj] == 1:
            if k < K:
                visit[ni][nj] = visit[i][j] + 1
                queue.append([ni, nj, k+1])

        else:
            visit[ni][nj] = visit[i][j] + 1
            queue.append([ni, nj, k])

        if ni == N-1 and nj == M-1:
            queue = None
            break

print(visit[-1][-1] if visit[-1][-1] else -1)