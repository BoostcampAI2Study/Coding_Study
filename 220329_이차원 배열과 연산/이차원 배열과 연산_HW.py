import sys, collections

R, C, K = map(int, sys.stdin.readline().strip().split())
a = [[0] * 100 for _ in range(100)]
for i in range(3):
    a[i] = list(map(int, sys.stdin.readline().strip().split())) + [0] * 97

def cal_min_time():
    len_r, len_c = 3, 3
    for t in range(101):
        if a[R - 1][C - 1] == K:
            return t
        # R 연산
        if len_r >= len_c:
            len_c = 0
            for r in range(len_r):
                count_row = sorted(collections.Counter(a[r]).most_common(), key=lambda x: (x[1], x[0]))
                for elements in count_row:
                    if elements[0] == 0:
                        count_row.remove(elements)
                        break
                new_row = []
                for i in range(len(count_row)):
                    if len(new_row) == 100:
                        break
                    new_row.append(count_row[i][0])
                    new_row.append(count_row[i][1])
                a[r] = new_row + [0] * (100 - len(new_row))
                len_c = len(new_row) if len_c < len(new_row) else len_c
        # C 연산
        else:
            tmp_r = 0
            for c in range(len_c):
                col = [a[r][c] for r in range(len_r)]
                count_col = sorted(collections.Counter(col).most_common(), key=lambda x: (x[1], x[0]))
                for elements in count_col:
                    if elements[0] == 0:
                        count_col.remove(elements)
                        break
                new_col = []
                for i in range(len(count_col)):
                    if len(new_col) == 100:
                        break
                    new_col.append(count_col[i][0])
                    new_col.append(count_col[i][1])
                for r in range(len(new_col)):
                    a[r][c] = new_col[r]
                for r in range(len(new_col), 100):
                    a[r][c] = 0
                tmp_r = len(new_col) if tmp_r < len(new_col) else tmp_r
            len_r = tmp_r
    return -1

print(cal_min_time())
