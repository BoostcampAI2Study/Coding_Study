import collections
def solution(board):
    N, directions = len(board), [(1, 0), (-1, 0), (0, 1), (0, -1)]
    min_build_costs = [[[2e6]*N for _ in range(N)] for _ in range(4)] # dir_idx, y, x
    Q = collections.deque([(0, 0, -1, 0)])
    while Q:
        y, x, prev_dir_idx, build_costs = Q.popleft()
        
        for dir_idx in range(4):
            new_y, new_x = y+directions[dir_idx][0], x+directions[dir_idx][1]
            
            if 0 <= new_y < N and 0 <= new_x < N and board[new_y][new_x] == 0:
                if prev_dir_idx == -1 or prev_dir_idx == dir_idx:
                    new_build_costs = build_costs + 100
                else:
                    new_build_costs = build_costs + 100 + 500

                if min_build_costs[dir_idx][new_y][new_x] > new_build_costs:
                    min_build_costs[dir_idx][new_y][new_x] = new_build_costs
                    if (new_y, new_x) != (N-1, N-1):
                        Q.append((new_y, new_x, dir_idx, new_build_costs))
    
    return min(min_build_costs[0][N-1][N-1], min_build_costs[1][N-1][N-1], min_build_costs[2][N-1][N-1], min_build_costs[3][N-1][N-1])