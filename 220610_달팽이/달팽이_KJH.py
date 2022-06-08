N = int(input())
goal = int(input())

board = [[None] * N for _ in range(N)]

direction = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
r, c = 0, 0
num = N ** 2
dir = 0
answer = None
while num > 0:
    board[r][c] = num
    if num == goal:
        answer = f"{r+1} {c+1}"
    dr, dc = direction[dir]
    nr, nc = r + dr, c + dc
    if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == None:
        r, c = nr, nc
    else:
        dir = (dir + 1) % 4
        dr, dc = direction[dir]
        nr, nc = r + dr, c + dc
        r, c = nr, nc
    num -= 1


for i in range(len(board)):
    board[i] = " ".join(map(str, board[i]))

for b in board:
    print(b)

print(answer)
