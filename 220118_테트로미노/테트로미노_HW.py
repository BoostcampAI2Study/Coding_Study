n, m = map(int, input().split())
board = [[int(i) for i in input().split()] for j in range(n)]

tet_list = [[(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)],
            [(0, 1), (1, 0), (1, 1)],
            [(1, 0), (2, 0), (2, 1)], [(0, 1), (0, 2), (-1, 2)], [(0, 1), (1, 1), (2, 1)],
            [(-1, 0), (-1, 1), (-1, 2)], [(0, 1), (-1, 1), (-2, 1)], [(0, 1), (0, 2), (1, 2)],
            [(0, -1), (1, -1), (2, -1)], [(1, 0), (1, 1), (1, 2)],
            [(1, 0), (1, 1), (2, 1)], [(0, 1), (-1, 1), (-1, 2)],
            [(1, 0), (1, -1), (2, -1)], [(0, 1), (1, 1), (1, 2)],
            [(0, 1), (-1, 1), (0, 2)], [(0, 1), (1, 1), (0, 2)],
            [(1, 0), (1, 1), (2, 0)], [(1, 0), (1, -1), (2, 0)]]

def find_max(x, y):
    tmp, res = 0, 0
    for tet in tet_list:
        tmp = board[x][y]
        for nx, ny in tet:
            nx, ny = x + nx, y + ny
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            tmp += board[nx][ny]
        if res < tmp:
            res = tmp
    return res

result = 0
for x in range(n):
    for y in range(m):
        tmp_res = find_max(x, y)
        if result < tmp_res:
            result = tmp_res
print(result)