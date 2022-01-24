from collections import deque

N, M, K = map(int, input().split())
inits = [[5] * N for _ in range(N)]
A = [[int(s) for s in input().split()] for _ in range(N)]
maps = [[deque() for _ in range(N)] for _ in range(N)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

for i in range(M):
    r, c, a = map(int, input().split())
    maps[r - 1][c - 1].append(a) # initial ages

def spring():
    for i in range(N):
        for j in range(N):
            for k in range(len(maps[i][j])):
                if maps[i][j][k] <= inits[i][j]:
                    inits[i][j] -= maps[i][j][k]
                    maps[i][j][k] += 1
                else:
                    while k < len(maps[i][j]):
                        inits[i][j] += (maps[i][j].pop() // 2)
                    break

def fall():
    for i in range(N):
        for j in range(N):
            for age in maps[i][j]:
                if age % 5 == 0:
                    for dir in dirs:
                        nx = i + dir[0]
                        ny = j + dir[1]

                        if 0 <= nx < N and 0 <= ny < N:
                            maps[nx][ny].appendleft(1)

def winter():
    for i in range(N):
        for j in range(N):
            inits[i][j] += A[i][j]

cnt = 0
while cnt < K:
    spring()
    fall()
    winter()
    cnt += 1

ans = 0
for i in range(N):
    for j in range(N):
        for age in maps[i][j]:
            if age > 0:
                ans += 1

print(ans)


# 5 2 1
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 1 3
# 3 2 3
