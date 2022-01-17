# -- 틀린 답
from collections import defaultdict
def solution(color_mat, mat, markers):
    cnt = 1
    data = {marker[:2]: [(idx, marker[2])] for idx, marker in enumerate(markers)}
    nxt_data = data.copy()
    while True:
        for marker in data.keys():
            cur_row, cur_col = marker

            idx, d = nxt_data[marker][0]
            d_row, d_col = direction[d]
            nxt_row, nxt_col = cur_row + d_row, cur_col + d_col

            if 0 <= nxt_row < N and 0 <= nxt_col < N and not color_mat[nxt_row][nxt_col] == 2:
                color = color_mat[nxt_row][nxt_col]
                if color == 0: # white
                    mat[nxt_row][nxt_col] += mat[cur_row][cur_col]
                    mat[cur_row][cur_col] = list()
                    if (nxt_row, nxt_col) not in nxt_data:
                        nxt_data[(nxt_row, nxt_col)] = list()
                    nxt_data[(nxt_row, nxt_col)] += nxt_data[marker]
                    del nxt_data[marker]
                elif color == 1: # red
                    mat[nxt_row][nxt_col] += mat[cur_row][cur_col][::-1]
                    mat[cur_row][cur_col] = list()
                    if (nxt_row, nxt_col) not in nxt_data:
                        nxt_data[(nxt_row, nxt_col)] = list()
                    nxt_data[(nxt_row, nxt_col)] += nxt_data[marker][::-1]
                    del nxt_data[marker]
            else: # out
                d_row, d_col = direction[reverse_direction[d]]
                nxt_row, nxt_col = cur_row + d_row, cur_col + d_col
                mat[cur_row][cur_col][0] = (idx, reverse_direction[d])
                if color_mat[nxt_row][nxt_col] == 2:
                    nxt_data[marker][0] = (idx, reverse_direction[d])
                else:
                    mat[nxt_row][nxt_col] += mat[cur_row][cur_col]
                    mat[cur_row][cur_col] = list()
                    if (nxt_row, nxt_col) not in nxt_data:
                        nxt_data[(nxt_row, nxt_col)] = list()
                    nxt_data[(nxt_row, nxt_col)] += nxt_data[marker]
                    del nxt_data[marker]
            if cnt > 1000:
                return -1
        for marker in nxt_data.keys():
            if len(nxt_data[marker]) >= 4:
                return cnt
        cnt += 1 # next turn
        data = nxt_data.copy()
        nxt_data = data.copy()

if __name__ == '__main__':
    N, K = map(int, input().split())
    color_mat = [list(map(int, input().split())) for _ in range(N)]
    markers = []
    for i in range(K):
        x, y, z = map(int, input().split())
        markers.append((x-1, y-1, z))
    mat = [[list() for _ in range(N)] for _ in range(N)]
    for idx, marker in enumerate(markers):
        row, col, d = marker
        mat[row][col].append((idx, d))

    direction = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
    reverse_direction = {1: 2, 2: 1, 3: 4, 4: 3}
    print(solution(color_mat, mat, markers))

# -- 정답
import sys

input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move(chess_num):
    x, y, z = chess[chess_num]
    if chess_num != chess_map[x][y][0]:
        return 0

    nx = x + dx[z]
    ny = y + dy[z]

    if not 0 <= nx < n or not 0 <= ny < n or a[nx][ny] == 2:
        if 0 <= z <= 1:
            nz = (z+1) % 2
        else:
            nz = (z-1) % 2 + 2
        chess[chess_num][2] = nz
        nx = x + dx[nz]
        ny = y + dy[nz]
        if not 0 <= nx < n or not 0 <= ny < n or a[nx][ny] == 2:
            return 0

    chess_set = []
    chess_set.extend(chess_map[x][y])
    chess_map[x][y] = []

    if a[nx][ny] == 1:
        chess_set = chess_set[-1::-1]

    for i in chess_set:
        chess_map[nx][ny].append(i)
        chess[i][:2] = [nx, ny]

    if len(chess_map[nx][ny]) >= 4:
        return 1
    return 0

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
chess_map = [[[] for _ in range(n)] for _ in range(n)]
chess = [0 for _ in range(k)]

for i in range(k):
    x, y, z = map(int, input().split())
    chess_map[x-1][y-1].append(i)
    chess[i] = [x-1, y-1, z-1]

cnt = 1
while cnt <= 1000:
    for i in range(k):
        flag = move(i)
        if flag:
            print(cnt)
            sys.exit()
    cnt += 1
print(-1)