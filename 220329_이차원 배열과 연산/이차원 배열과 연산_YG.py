from collections import defaultdict
import sys
input = sys.stdin.readline

# 원하는 답
t_x, t_y, target = map(int, input().split())
t_x -= 1
t_y -= 1

# 크기 초기화
r, c = 3, 3

# 입력
arr = [[0]*100 for _ in range(100)]
for x in range(3):
    sub = list(map(int, input().split()))
    for y in range(3):
        arr[x][y] = sub[y]

def operater(arr, value):
    next_value = 0
    sorted_arr = []
    for x in range(value):
        db = defaultdict(int)
        # (수, 등장횟수)
        for a in arr[x]:
            if a != 0:
                db[a] += 1

        counter = []
        for idx in db:
            counter.append([idx, db[idx]])

        counter.sort(key = lambda x : (x[1], x[0]))
        #print(counter)
        next_row = []
        for a, b in counter:
            next_row += [a, b]
        # 100 넘어가면 버림
        if len(next_row) >= 100:
            next_row = next_row[:100]
        sorted_arr.append(next_row)
        next_value = max(next_value, len(next_row))


    return next_value, sorted_arr

# for문 실행
for time in range(101):
    # 원하는 답과 일치하면 정답 출력 후 break
    if arr[t_x][t_y] == target:
        print(time)
        break

    # R 연산
    if r >= c:
        next_c, sorted_arr = operater(arr, r)
        c = next_c
        arr = [[0]*100 for _ in range(100)]
        for x in range(len(sorted_arr)):
            for y in range(len(sorted_arr[x])):
                arr[x][y] = sorted_arr[x][y]

    # C 연산
    else:
        n_arr = [[0]*100 for _ in range(100)]
        for x in range(r):
            for y in range(c):
                n_arr[y][x] = arr[x][y]
        next_r, sorted_arr = operater(n_arr, c)
        r = next_r

        arr = [[0]*100 for _ in range(100)]
        n_arr = [[0]*100 for _ in range(100)]

        for x in range(len(sorted_arr)):
            for y in range(len(sorted_arr[x])):
                n_arr[x][y] = sorted_arr[x][y]

        for x in range(c):
            for y in range(r):
                arr[y][x] = n_arr[x][y]


# 100초가 지나면 -1 출력
else:
    print(-1)
