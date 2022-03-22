import sys, collections

N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(N)]
hole, R, B = 0, 0, 0

for r in range(N):
    for c in range(M):
        if board[r][c] == 'R':
            R = (r, c)
        if board[r][c] == 'B':
            B = (r, c)

NR = [0, 0, 1, -1]
NC = [1, -1, 0, 0]

visit = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
q = collections.deque()
q.append((R, B, 0))
visit[R[0]][R[1]][B[0]][B[1]] = True
answer = 1e9

while q:
    (red_r, red_c), (blue_r, blue_c), move = q.popleft()
    if move > 10:
        continue

    for i in range(4):
        new_red_r, new_red_c, new_blue_r, new_blue_c = red_r, red_c, blue_r, blue_c
        red_move, blue_move = 0, 0
        is_red_hole, is_blue_hole = False, False

        # red
        while True:
            red_move += 1
            if board[new_red_r + NR[i]][new_red_c + NC[i]] == "#":
                break
            else:
                new_red_r, new_red_c = new_red_r + NR[i], new_red_c + NC[i]
            if board[new_red_r][new_red_c] == "O":
                is_red_hole = True
                break
        # blue
        while True:
            blue_move += 1
            if board[new_blue_r + NR[i]][new_blue_c + NC[i]] == "#":
                break
            else:
                new_blue_r, new_blue_c = new_blue_r + NR[i], new_blue_c + NC[i]
            if board[new_blue_r][new_blue_c] == "O":
                is_blue_hole = True
                break

        if is_red_hole and not is_blue_hole:
            answer = min(answer, move + 1)
            break
        if not is_red_hole and not is_blue_hole:
            if visit[new_red_r][new_red_c][new_blue_r][new_blue_c]:
                continue
            if new_red_r == new_blue_r and new_red_c == new_blue_c:
                if red_move < blue_move:
                    new_blue_r, new_blue_c = new_blue_r - NR[i], new_blue_c - NC[i]
                else:
                    new_red_r, new_red_c = new_red_r - NR[i], new_red_c - NC[i]

            q.append(((new_red_r, new_red_c),(new_blue_r, new_blue_c), move + 1))
            visit[new_red_r][new_red_c][new_blue_r][new_blue_c] = True

print(answer) if answer <= 10 else print(-1)
