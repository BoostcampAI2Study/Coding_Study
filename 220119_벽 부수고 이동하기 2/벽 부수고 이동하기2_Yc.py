from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().strip().split())

WALLS = []
for _ in range(N):
    WALLS.append(input().strip())

moves = [[1,0],[0,1],[-1,0],[0,-1]]
visit_distance = [[[-1] * (M) for _ in range(N)] for _ in range(K+1)]

visit_distance[0][0][0] = 1 
queue = deque([(0,0,0)])    # break_wall count, row, col

answer = -1
while queue:
    break_wall, row, col = queue.popleft()

    if row == N-1 and col == M-1:
        answer = visit_distance[break_wall][row][col]
        break

    for mr, mc in moves:
        new_row, new_col = mr+row, mc+col
        if 0 <= new_row < N and 0 <= new_col < M:
            if WALLS[new_row][new_col]=='1': 
                if break_wall < K and visit_distance[break_wall+1][new_row][new_col] == -1:
                    visit_distance[break_wall+1][new_row][new_col] = visit_distance[break_wall][row][col]+1
                    queue.append((break_wall+1, new_row, new_col))
            else: 
                if visit_distance[break_wall][new_row][new_col] == -1:
                    visit_distance[break_wall][new_row][new_col] = visit_distance[break_wall][row][col]+1
                    queue.append((break_wall, new_row, new_col))

print(answer)