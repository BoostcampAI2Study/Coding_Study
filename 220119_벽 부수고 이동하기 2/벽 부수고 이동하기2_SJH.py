from collections import deque
from sys import stdin

def can_visit(i, j, k):
    return 0 <= i < N and 0 <= j < M and not visit[i][j][k]


def bfs(start):
    queue = deque([start])
    move = ((-1, 0), (0, 1), (1, 0), (0, -1))

    while queue:
        i, j, k = queue.popleft()
        dist = visit[i][j][k] + 1

        # 목적지!
        if i == N-1 and  j == M-1:
            return visit[i][j][k]

        for _i, _j  in move:
            ni, nj = i + _i, j + _j

            # 범위 체크
            if can_visit(ni, nj, k):              
                # 벽 x
                if not board[ni][nj]:
                    visit[ni][nj][k] = dist
                    queue.append((ni, nj, k))
                    

                # 벽이고 부술 수 있음
                elif k < K:
                    visit[ni][nj][k+1] = dist
                    queue.append((ni, nj, k+1))

    return -1


if __name__ == '__main__':
    N, M, K = map(int, stdin.readline().split())
    board = [list(map(int, stdin.readline().strip())) for n in range(N)]

    visit = [[[0] * (K+1) for m in range(M)] for n in range(N)]
    visit[0][0] = [1]  * (K+1)

    print(bfs((0, 0, 0)))