N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

NR = [1, -1, 0, 0]
NC = [0, 0, 1, -1]
min_click = 11

def dfs(main_button, sub_button, click):
    global min_click
    main_r, main_c = main_button
    sub_r, sub_c = sub_button

    if click > 10:
        return

    for i in range(4):
        nr, nc = NR[i] + main_r, NC[i] + main_c
        sub_nr, sub_nc = NR[i] + sub_r, NC[i] + sub_c
        if sub_nr < 0 or sub_nc < 0 or sub_nr >= N or sub_nc >= M:
            continue
        if nr < 0 or nc < 0 or nr >= N or nc >= M:
            if click < min_click:
                min_click = click + 1
            continue
        
        if board[sub_nr][sub_nc] == "#":
            sub_nr, sub_nc = sub_r, sub_c

        if board[nr][nc] != "#":
            dfs([nr, nc], [sub_nr, sub_nc], click + 1)
        else:
            dfs([main_r, main_c], [sub_nr, sub_nc], click + 1)

buttons = []
# button 위치 찾기
for r in range(N):
    for c in range(M):
        if board[r][c] == 'o':
            buttons.append([r, c])
# button dfs
for i in range(2):
    dfs(buttons[i], buttons[1 - i], 0)

print(min_click) if min_click != 11 else print(-1)
