
from collections import defaultdict, deque
from copy import deepcopy
from itertools import permutations


def solution(board, r, c):
    answer = float("inf")

    card_pos = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card_pos[board[i][j]].append((i, j))

    def move_ctrl(x, y, dx, dy, board):
        x += dx
        y += dy
        while 0 <= x < 4 and 0 <= y < 4:
            if board[x][y] != 0:
                return x, y
            x += dx
            y += dy
        return x - dx, y - dy

    def bfs(cur_pos, first_card_pos, color, BOARD, check_first_card_distance=False):
        visited = [[0] * 4 for _ in range(4)]
        q = deque([(cur_pos, 0)])
        while q:
            (x, y), cnt = q.popleft()
            if visited[x][y]:
                continue
            if check_first_card_distance:
                if (x, y) == first_card_pos:
                    return x, y, cnt + 1, BOARD
            else:
                if BOARD[x][y] == color and (x, y) != first_card_pos:
                    BOARD[x][y] = BOARD[first_card_pos[0]][first_card_pos[1]] = 0
                    return x, y, cnt + 1, BOARD
            visited[x][y] = 1
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                c_nx, c_ny = move_ctrl(x, y, dx, dy, BOARD)

                q.append(((c_nx, c_ny), cnt + 1))
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not visited[nx][ny]:
                        q.append(((nx, ny), cnt + 1))

    def dfs(order_idx, R, C, cnt, board):
        nonlocal answer
        if order_idx == len(order):
            answer = min(cnt, answer)
            return
        if cnt > answer:
            return
        color = order[order_idx]
        for i in [0, 1]:
            first_card_pos = card_pos[color][i]
            n_R, n_C, s_cnt, _ = bfs((R, C), first_card_pos, color, board, True)
            n_R, n_C, CNT, n_board = bfs(
                (n_R, n_C), first_card_pos, color, deepcopy(board)
            )
            dfs(order_idx + 1, n_R, n_C, CNT + cnt + s_cnt, deepcopy(n_board))

    for order in permutations(list(card_pos.keys()), len(card_pos)):
        R, C = r, c
        dfs(0, R, C, 0, deepcopy(board))

    return answer
