def solution(board, aloc, bloc):
    answer = -1
    N, M = len(board), len(board[0])
    dydx = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def dfs(move_cnt, cur_player_y, cur_player_x, next_player_y, next_player_x):
        nonlocal board, N, M
        cur_player_win = False
        winner_min_move_cnt = 5*5
        loser_max_move_cnt = move_cnt
        
        if board[cur_player_y][cur_player_x]:
            for idx in range(4):
                player_after_next_y, player_after_next_x = cur_player_y+dydx[idx][0], cur_player_x+dydx[idx][1]
                if 0 <= player_after_next_y < N and 0 <= player_after_next_x < M and board[player_after_next_y][player_after_next_x]:
                    board[cur_player_y][cur_player_x] = 0
                    
                    next_player_win, next_player_move_cnt = dfs(move_cnt+1, next_player_y, next_player_x, player_after_next_y, player_after_next_x)
                    if not next_player_win:
                        cur_player_win = True
                        
                    if next_player_win:
                        loser_max_move_cnt = max(loser_max_move_cnt, next_player_move_cnt)
                    else:
                        winner_min_move_cnt = min(winner_min_move_cnt, next_player_move_cnt)
                    
                    board[cur_player_y][cur_player_x] = 1
        
        return cur_player_win, winner_min_move_cnt if cur_player_win else loser_max_move_cnt
        
    
    return dfs(0, aloc[0], aloc[1], bloc[0], bloc[1])[1]
