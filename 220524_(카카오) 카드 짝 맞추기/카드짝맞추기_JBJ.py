import sys, collections
def solution(board, r, c):
    dydx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    CARDS = collections.defaultdict(list)
    for y in range(4):
        for x in range(4):
            if board[y][x]:
                CARDS[board[y][x]].append((y, x))
    
    def get_min_time(start_coordinates, destination_coordinates):
        nonlocal board, dydx
        
        sc_y, sc_x = start_coordinates
        dc_y, dc_x = destination_coordinates
        visited = [[False]*4 for _ in range(4)]
        
        Q = collections.deque([(sc_y, sc_x, 0)])
        visited[sc_y][sc_x] = True
        while Q:
            y, x, elapsed_time = Q.popleft()

            if y == dc_y and x == dc_x:
                return elapsed_time + 1 # destination enter time
            
            for idx in range(4):
                normal_move_y, normal_move_x = y+dydx[idx][0], x+dydx[idx][1] # normal move
                if 0 <= normal_move_y < 4 and 0 <= normal_move_x < 4 and not visited[normal_move_y][normal_move_x]:
                    visited[normal_move_y][normal_move_x] = True
                    Q.append((normal_move_y, normal_move_x, elapsed_time+1))
                
                ctrl_move_y, ctrl_move_x = y, x # ctrl move
                while True:
                    ctrl_move_y, ctrl_move_x = ctrl_move_y+dydx[idx][0], ctrl_move_x+dydx[idx][1]
                    if not (0 <= ctrl_move_y < 4 and 0 <= ctrl_move_x < 4):
                        ctrl_move_y, ctrl_move_x = ctrl_move_y-dydx[idx][0], ctrl_move_x-dydx[idx][1]
                        break
                    elif board[ctrl_move_y][ctrl_move_x] != 0:
                        break
                        
                if not visited[ctrl_move_y][ctrl_move_x]:
                    visited[ctrl_move_y][ctrl_move_x] = True
                    Q.append((ctrl_move_y, ctrl_move_x, elapsed_time+1))
    
    def solve(sr, sc, card_cnt):
        nonlocal board, CARDS
        
        if card_cnt == 0: return 0
    
        min_time = sys.maxsize
        for card_idx, (card_1, card_2) in CARDS.items():
            if board[card_1[0]][card_1[1]] == 0 and board[card_2[0]][card_2[1]] == 0: continue
            
            card_1_elapsed_time = get_min_time((sr, sc), card_1) + get_min_time(card_1, card_2)
            card_2_elapsed_time = get_min_time((sr, sc), card_2) + get_min_time(card_2, card_1)

            board[card_1[0]][card_1[1]], board[card_2[0]][card_2[1]] = 0, 0
            min_time = min(min_time, card_1_elapsed_time + solve(card_2[0], card_2[1], card_cnt-1))
            min_time = min(min_time, card_2_elapsed_time + solve(card_1[0], card_1[1], card_cnt-1))
            board[card_1[0]][card_1[1]], board[card_2[0]][card_2[1]] = card_idx, card_idx
        
        return min_time
    
    return solve(r, c, len(CARDS.keys()))