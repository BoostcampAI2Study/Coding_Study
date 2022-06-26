import sys
cnt = 1
DIRECTION = {'U': (-1, 0),'D': (1, 0),'L': (0, -1),'R': (0, 1)}
while True:
    R, C = map(int, sys.stdin.readline().split())
    if R == 0 and C == 0:
        break
    STATUS = [list(sys.stdin.readline().strip()) for _ in range(R)]
    KEYS = sys.stdin.readline().strip()

    cur_r, cur_c, goals = 0, 0, []
    for r in range(R):
        for c in range(C):
            if STATUS[r][c] == 'w' or STATUS[r][c] == 'W':
                cur_r, cur_c = r, c
            if STATUS[r][c] == '+' or STATUS[r][c] == 'W' or STATUS[r][c] == 'B':
                goals.append([r, c])

    is_complete = True
    for d in KEYS:
        nr, nc = cur_r + DIRECTION[d][0], cur_c + DIRECTION[d][1]
        if 0 <= nr < R and 0 <= nc < C and STATUS[nr][nc] != '#':
            if STATUS[nr][nc] == 'b' or STATUS[nr][nc] == 'B':
                box_nr, box_nc = nr + DIRECTION[d][0], nc + DIRECTION[d][1]
                if 0 <= box_nr < R and 0 <= box_nc < C and (STATUS[box_nr][box_nc] == '.' or STATUS[box_nr][box_nc] == '+'):
                    STATUS[box_nr][box_nc] = 'b'
                    STATUS[nr][nc] = 'w'
                    STATUS[cur_r][cur_c] = '.'
                    cur_r, cur_c = nr, nc
            else:
                STATUS[nr][nc] = 'w'
                STATUS[cur_r][cur_c] = '.'
                cur_r, cur_c = nr, nc
        
        is_complete = True
        for g in goals:
            g_r, g_c = g
            if STATUS[g_r][g_c] == 'b' or STATUS[g_r][g_c] == 'B':
                continue
            else:
                is_complete = False
                break
        if is_complete:
            break
    
    for g in goals:
        g_r, g_c = g
        if STATUS[g_r][g_c] == '.':
            STATUS[g_r][g_c] = '+'
        if STATUS[g_r][g_c] == 'b':
            STATUS[g_r][g_c] = 'B'
        if STATUS[g_r][g_c] == 'w':
            STATUS[g_r][g_c] = 'W'

    print("Game %d: complete" % cnt) if is_complete else print("Game %d: incomplete" % cnt)
    for s in STATUS:
        print(''.join(list(map(str, s))))
    cnt += 1
