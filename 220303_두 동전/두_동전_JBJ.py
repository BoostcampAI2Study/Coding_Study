import heapq, sys
N, M = map(int, sys.stdin.readline().strip().split())
BOARD = [sys.stdin.readline().strip() for _ in range(N)]
DY = [0, 0, 1, -1]
DX = [1, -1, 0, 0]

answer = -1
heap = [[0]] # button click count
visited = set()
heap[0].extend(sum([[n, m] for n in range(N) for m in range(M) if BOARD[n][m] == 'o'], []))

while heap:
    button_click_cnt, coin_1_y, coin_1_x, coin_2_y, coin_2_x = heapq.heappop(heap)
    if button_click_cnt > 10: 
        break
    visited.add((coin_1_y, coin_1_x, coin_2_y, coin_2_x))

    out_of_board = 0
    if not (0 <= coin_1_y < N) or not (0 <= coin_1_x < M):
        out_of_board += 1
    if not (0 <= coin_2_y < N) or not (0 <= coin_2_x < M):
        out_of_board += 1
    
    if out_of_board == 1:
        answer = button_click_cnt
        break
    elif out_of_board == 0:
        for idx in range(4):
            coin_1_new_y, coin_1_new_x, coin_2_new_y, coin_2_new_x = coin_1_y+DY[idx], coin_1_x+DX[idx], coin_2_y+DY[idx], coin_2_x+DX[idx]
            if 0 <= coin_1_new_y < N and 0 <= coin_1_new_x < M and BOARD[coin_1_new_y][coin_1_new_x] == '#':
                coin_1_new_y, coin_1_new_x = coin_1_y, coin_1_x
            if 0 <= coin_2_new_y < N and 0 <= coin_2_new_x < M and BOARD[coin_2_new_y][coin_2_new_x] == '#':
                coin_2_new_y, coin_2_new_x = coin_2_y, coin_2_x

            if (coin_1_new_y, coin_1_new_x, coin_2_new_y, coin_2_new_x) not in visited:
                heapq.heappush(heap, [button_click_cnt+1, coin_1_new_y, coin_1_new_x, coin_2_new_y, coin_2_new_x])

print(answer)