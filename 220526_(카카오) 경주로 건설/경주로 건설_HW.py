from collections import deque
def solution(board):
    answer = 1e9
    N = len(board)
    NR, NC = [0, 0, 1, -1], [1, -1, 0, 0]
    rev_directions = {0:1, 1:0, 2:3, 3:2}
    
    q = deque()
    q.append((0, 0, 0, -1)) # r, c, cost, prev_direction
    visit = [[[1e9] * N for _ in range(N)] for _ in range(4)]
    
    while q:
        r, c, cost, prev_direction = q.popleft()
        if r == N - 1 and c == N - 1:
            answer = min(answer, cost)
        for i in range(4):
            nr, nc = r + NR[i], c + NC[i]
            if 0 <= nr < N and 0 <= nc < N and not board[nr][nc]:
                if prev_direction == i or prev_direction == -1 and cost + 100 < visit[i][nr][nc]:
                    q.append((nr, nc, cost + 100, i))
                    visit[i][nr][nc] = cost + 100
                elif rev_directions[prev_direction] != i and cost + 600 < visit[i][nr][nc]:
                    q.append((nr, nc, cost + 600, i))
                    visit[i][nr][nc] = cost + 600
    
    return answer
