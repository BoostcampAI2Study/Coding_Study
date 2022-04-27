from collections import deque, defaultdict
from itertools import permutations, product

min_result = 1e9        
def solution(board, r, c):
    def bfs(start, end):
        NR = [0, 0, 1, -1]
        NC = [1, -1, 0, 0]
        q = deque()
        q.append((start[0], start[1], 0))
        while q:
            r, c, move = q.popleft()
            if r == end[0] and c == end[1]:
                return move
            
            for i in range(4):
                nr, nc = r + NR[i], c + NC[i]
                if 0 <= nr < 4 and 0 <= nc < 4:
                    q.append((nr, nc, move + 1))
                    if board[nr][nc] > 0:
                        continue
                    # ctrl
                    while True:
                        if 0 <= nr + NR[i] < 4 and 0 <= nc + NC[i] < 4:
                            nr, nc = nr + NR[i], nc + NC[i]
                            if board[nr][nc] > 0:
                                q.append((nr, nc, move + 1))
                                break
                            continue
                        elif 0 <= nr < 4 and 0 <= nc < 4:
                            q.append((nr, nc, move + 1))
                        break
    
    def dfs(sequence, cur_loc, cnt_idx, move):
        global min_result
        if cnt_idx == len(sequence):
            min_result = min(min_result, move)
            return
        
        for i in range(2):
            cur_move = bfs(cur_loc, cards_location[sequence[cnt_idx]][i])
            board[cards_location[sequence[cnt_idx]][i][0]][cards_location[sequence[cnt_idx]][i][1]] = 0
            
            cur_move += bfs(cards_location[sequence[cnt_idx]][i], cards_location[sequence[cnt_idx]][1 - i])
            board[cards_location[sequence[cnt_idx]][1 - i][0]][cards_location[sequence[cnt_idx]][1 - i][1]] = 0
            
            dfs(sequence, cards_location[sequence[cnt_idx]][1 - i], cnt_idx + 1, move + cur_move + 2)
            
            board[cards_location[sequence[cnt_idx]][i][0]][cards_location[sequence[cnt_idx]][i][1]], board[cards_location[sequence[cnt_idx]][1 - i][0]][cards_location[sequence[cnt_idx]][1 - i][1]] = sequence[cnt_idx], sequence[cnt_idx]
                        
    cards_location = defaultdict(list)
    for cur_r in range(4):
        for cur_c in range(4):
            if board[cur_r][cur_c]:
                cards_location[board[cur_r][cur_c]].append([cur_r, cur_c])

    for sequence in permutations(list(cards_location.keys())):
        dfs(sequence, [r, c], 0, 0)
    
    return min_result
