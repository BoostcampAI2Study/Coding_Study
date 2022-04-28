def solution(board, aloc, bloc):
    answer = -1

    def move(a_r, a_c, b_r, b_c, board, cnt, player):
        if player == 1:
            r, c = a_r, a_c
        else:
            r, c = b_r, b_c

        win = False
        win_cnt = float("inf")
        fall_cnt = cnt
        if board[r][c]:
            board[r][c] = 0

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (
                    0 <= r + dx < len(board)
                    and 0 <= c + dy < len(board[0])
                    and board[r + dx][c + dy]
                ):
                    nr, nc = r + dx, c + dy
                    if player == 1:
                        a_r, a_c = nr, nc
                    else:
                        b_r, b_c = nr, nc
                    n_win, n_cnt = move(a_r, a_c, b_r, b_c, board, cnt + 1, player * -1)
                    if not n_win:
                        win = True
                        win_cnt = min(win_cnt, n_cnt)
                    else:
                        fall_cnt = max(fall_cnt, n_cnt)
            board[r][c] = 1

        return (True, win_cnt) if win else (False, fall_cnt)

    _, answer = move(aloc[0], aloc[1], bloc[0], bloc[1], board, 0, 1)

    return answer
