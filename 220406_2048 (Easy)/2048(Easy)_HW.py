import sys, collections
N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

q = collections.deque()
q.append((board, 0))
result = 0
while q:
    cur_board, move = q.popleft()
    # check max elements
    for r in range(N):
        for c in range(N):
            result = max(result, cur_board[r][c])
    if move >= 5:
        continue

    for k in range(4):
        if k < 2:
            update_board = []
        else:
            update_board = [[0] * N for _ in range(N)]

        # left & right
        if k < 2:
            for r in range(N):
                elements = [cur_board[r][c] for c in range(N) if cur_board[r][c]]
                new_raw = []
                if elements is None:
                    new_raw = [0] * N
                else:
                    # left
                    if k == 0:
                        i = 0
                        while i < len(elements):
                            if i < len(elements) - 1 and elements[i] == elements[i + 1]:
                                new_raw.append(elements[i] * 2)
                                i += 1
                            else:
                                new_raw.append(elements[i])
                            i += 1
                        new_raw = new_raw + [0] * (N - len(new_raw))
                    # right
                    else:
                        i = len(elements) - 1
                        while i >= 0:
                            if i > 0 and elements[i] == elements[i - 1]:
                                new_raw.append(elements[i] * 2)
                                i -= 1
                            else:
                                new_raw.append(elements[i])
                            i -= 1
                        new_raw = [0] * (N - len(new_raw)) + new_raw[::-1]
                update_board.append(new_raw)
        # up & down
        else:
            for c in range(N):
                elements = [cur_board[r][c] for r in range(N) if cur_board[r][c]]
                new_col = []
                if elements is None:
                    new_col = [0] * N
                else:
                    # up
                    if k == 2:
                        i = 0
                        while i < len(elements):
                            if i < len(elements) - 1 and elements[i] == elements[i + 1]:
                                new_col.append(elements[i] * 2)
                                i += 1
                            else:
                                new_col.append(elements[i])
                            i += 1
                        new_col = new_col + [0] * (N - len(new_col))
                    # down
                    else:
                        i = len(elements) - 1
                        while i >= 0:
                            if i > 0 and elements[i] == elements[i - 1]:
                                new_col.append(elements[i] * 2)
                                i -= 1
                            else:
                                new_col.append(elements[i])
                            i -= 1
                        new_col = [0] * (N - len(new_col)) + new_col[::-1]
                for r in range(N):
                    update_board[r][c] = new_col[r]

        if update_board != cur_board:
            q.append((update_board, move + 1))

print(result)
