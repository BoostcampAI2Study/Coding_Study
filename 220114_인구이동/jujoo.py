from collections import deque
def cal(cur_rcs):
    global mat
    people_num = sum([mat[cur_rc[0]][cur_rc[1]] for cur_rc in cur_rcs]) // len(cur_rcs)
    for cur_rc in cur_rcs:
        mat[cur_rc[0]][cur_rc[1]] = people_num

# -- 틀림
def solution():
    global time
    q = deque([[(0, 0)]])
    is_append = False
    while q:
        cur_rcs = q.popleft()

        if len(cur_rcs) == N * N:
            cal(cur_rcs)
            return  False
        print(cur_rcs)
        print(mat)
        for cur_rc in cur_rcs:
            row, col = cur_rc
            for d_row, d_col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nxt_row, nxt_col = row + d_row, col + d_col
                if (0 <= nxt_row < N and 0 <= nxt_col < N and (nxt_row, nxt_col) not in cur_rcs) \
                    and L <= abs(mat[row][col] - mat[nxt_row][nxt_col]) <= R:
                        q.append(cur_rcs + [(nxt_row, nxt_col)])
                        is_append = True

    if is_append:
        cal(cur_rcs)
        return False
    else: # 연합이 더 이상 없으면
        return True

if __name__ == '__main__':
    # N, L, R = map(int, input().split())
    N, L, R = 3, 5, 10
    mat = [[10, 15, 20], [20, 30, 25], [40, 22, 10]]
    # for _ in range(N):
        # mat.append(list(map(int, input().split())))
    time = 0
    while True:
        if solution():
            print(time)
            break
        else:
            time += 1