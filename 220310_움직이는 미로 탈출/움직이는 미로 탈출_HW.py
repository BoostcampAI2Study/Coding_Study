import collections
board = [input() for _ in range(8)]
visit = [[0] * 8 for _ in range(8)]
NR = [0, 0, 0, 1, -1, 1, 1, -1, -1]
NC = [0, 1, -1, 0, 0, 1, -1, 1, -1]

# character location = (7, 0)
q = collections.deque()
q.append((7, 0, 0))
result = 0
while q:
    for _ in range(len(q)):
        r, c, move = q.popleft()
        # goal = (0, 7)
        if r == 0 and c == 7:
            result = 1
            break

        # move character
        for i in range(9):
            nr, nc = r + NR[i], c + NC[i]
            if 0 <= nr < 8 and 0 <= nc < 8 and visit[nr][nc] < 8:
                if board[nr][nc] == ".":
                    if nr != 0 and board[nr - 1][nc] == "#":
                        continue
                    q.append((nr, nc, move + 1))
                    visit[nr][nc] += 1

    # move walls down
    del board[7]
    board.insert(0, '........')

print(result)
