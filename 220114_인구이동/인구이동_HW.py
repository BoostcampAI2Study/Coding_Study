import collections

def get_arr(arr, n, l, r):
    q1 = collections.deque()
    q2 = collections.deque()
    visit = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                q1.append((i, j))
                q2.append((i, j))
                visit[i][j] = -1

            # 국경 확인
            while q1:
                x, y = q1.popleft()
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if nx > n - 1 or nx < 0 or ny > n - 1 or ny < 0:
                        continue
                    if visit[nx][ny] != 0:
                        continue
                    if l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                        q1.append((nx, ny))
                        q2.append((nx, ny))
                        visit[nx][ny] = -1

            # 국경 열린 곳 인구 계산
            if len(q2) > 1:
                people = 0
                for x, y in q2:
                    people += arr[x][y]
                people_res = int(people / len(q2))
            elif len(q2) == 1:
                q2.popleft()

            # 국경 열린 곳 인구 이동
            while q2:
                x, y = q2.popleft()
                visit[x][y] = people_res

            if visit[x][y] == -1:
                visit[x][y] = arr[x][y]
    return visit

n, l, r = map(int, input().split())
arr = [[int(i) for i in input().split()] for j in range(n)]
cnt = 0
while arr:
    new_arr = get_arr(arr, n, l, r)
    if new_arr == arr:
        break
    else:
        arr = new_arr
        cnt += 1
print(cnt)