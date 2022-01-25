# wtf
# 포기!

d = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
}

# horizontal or vertical
dirs = [(0, 1), (1, 0)]

# whether v (digit) is possible to set
def is_possible(r, c, v):
    if v in maps[r]:
        return False

    for i in range(9):
        if v == maps[i][c]:
            return False

    tmp_r = (r // 3) * 3
    tmp_c = (c // 3) * 3
    for i in range(tmp_r, tmp_r + 3):
        for j in range(tmp_c, tmp_c + 3):
            if v == maps[i][j]:
                return False
    return True

def dfs(idx):
    r = idx // 9
    c = idx % 9

    # terminate
    if idx == 81:
        return

    # if not 0 => already set
    if maps[r][c]:
        dfs(idx + 1)

    for dir in dirs:
        nx = r + dir[0]
        ny = c + dir[1]

        if 0 <= nx < 9 and 0 <= ny < 9 and not maps[nx][ny]:
            for i in range(1, 10):
                for j in range(1, 10):
                    if i != j and not tiles[i][j] and is_possible(r, c, i) and is_possible(nx, ny, j):
                        tiles[i][j] = tiles[j][i] = True
                        maps[r][c] = i
                        maps[nx][ny] = j
                        dfs(idx + 1)
                        maps[r][c] = 0
                        maps[nx][ny] = 0
                        tiles[i][j] = tiles[j][i] = False

cnt = 1
while True:
    n = int(input())
    if not n:
        break

    tiles = [[False] * 10 for _ in range(10)]
    maps = [[0 for _ in range(9)] for _ in range(9)]
    for _ in range(n):
        dominos = input().split()
        r1 = d[dominos[1][0]]
        c1 = int(dominos[1][1]) - 1
        n1 = int(dominos[0])
        maps[r1][c1] = n1
        r2 = d[dominos[3][0]]
        c2 = int(dominos[3][1]) - 1
        n2 = int(dominos[2])
        maps[r2][c2] = n2
        tiles[n1][n2] = tiles[n2][n1] = True

    dominos = input().split()
    for i, domino in enumerate(dominos):
        r = d[domino[0]]
        c = int(domino[1]) - 1
        maps[r][c] = i + 1

    # sudoku
    dfs(0)
    print('Puzzle', cnt)
    for row in maps:
        print(''.join(map(str, row)))
    cnt += 1

# 10
# 6 B2 1 B3
# 2 C4 9 C3
# 6 D3 8 E3
# 7 E1 4 F1
# 8 B7 4 B8
# 3 F5 2 F6
# 7 F7 6 F8
# 5 G4 9 G5
# 7 I8 8 I9
# 7 C9 2 B9
# C5 A3 D9 I4 A9 E5 A2 C6 I1
