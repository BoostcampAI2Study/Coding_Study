def solution(board, aloc, bloc):
    def dfs(cur_loc, next_loc):
        player_win = False
        min_res, max_res = 1e9, 0
        
        r, c = cur_loc
        if board[r][c]: 
            board[r][c] = 0
            for nr, nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + nr, c + nc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc]:
                    next_player_win, next_move = dfs(next_loc, [nr, nc])
                    
                    if not next_player_win:
                        player_win = True
                        min_res = min(min_res, next_move + 1)
                    else:
                        max_res = max(max_res, next_move + 1)
            board[r][c] = 1
        
        return_move = min_res if player_win else max_res
        return player_win, return_move
    
    return dfs(aloc, bloc)[1]
