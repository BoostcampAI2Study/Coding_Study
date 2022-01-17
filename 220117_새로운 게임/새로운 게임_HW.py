n, k = map(int, input().split())
board = [[int(i) for i in input().split()] for j in range(n)]
pieces = [tuple(int(x) for x in input().split()) for j in range(k)]

dir_dict = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
rev_dict = {1: 2, 2: 1, 3: 4, 4: 3}

loc_list, piece_list = [], []
for piece in pieces:
    loc_list.append((piece[0] - 1, piece[1] - 1))
    piece_list.append((piece[2], 1))

cnt = 0
while cnt <= 1000:
    cnt += 1  # count turn
    for i in range(k):
        direct, rank = piece_list[i]
        x, y = loc_list[i]
        if rank != 1:
            continue
        nx, ny = x + dir_dict[direct][0], y + dir_dict[direct][1]

        # 파랑 & 체스판 벗어나는 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 2:
            # 말의 방향 변경
            direct = rev_dict[direct]
            piece_list[i] = (direct, rank)
            # 이동
            nx, ny = x + dir_dict[direct][0], y + dir_dict[direct][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

        loc_cnt = loc_list.count((nx, ny))
        # 하양
        if board[nx][ny] == 0:
            for j in range(k):
                if loc_list[j] == (x, y):
                    loc_list[j] = (nx, ny)
                    piece_list[j] = (piece_list[j][0], piece_list[j][1] + loc_cnt)
        # 빨강
        elif board[nx][ny] == 1:
            now_loc_cnt = loc_list.count((x, y))
            # reverse rank
            for j in range(k):
                if loc_list[j] == (x, y):
                    piece_list[j] = (piece_list[j][0], now_loc_cnt - piece_list[j][1] + loc_cnt + 1)
                    loc_list[j] = (nx, ny)

        # 4개 이상 모인 경우 종료
        loc_cnt = loc_list.count((nx, ny))
        if loc_cnt >= 4:
            print(cnt)
            exit()

print(-1)