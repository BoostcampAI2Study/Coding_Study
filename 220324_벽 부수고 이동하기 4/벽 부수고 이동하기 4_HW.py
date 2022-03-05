import sys, collections
sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())
MAP = [list(map(int, input())) for _ in range(N)]
sub_map = [[0] * M for _ in range(N)]
result = [[0] * M for _ in range(N)]
num = 1

NR = [0, 0, 1, -1]
NC = [1, -1, 0, 0]

def dfs(r, c):
    if MAP[r][c] == 1:
        return
    sub_map[r][c] = num
    for i in range(4):
        nr, nc = r + NR[i], c + NC[i]
        if 0 <= nr < N and 0 <= nc < M and sub_map[nr][nc] == 0:
            dfs(nr, nc)

for r in range(N):
    for c in range(M):
        if MAP[r][c] != 1 and sub_map[r][c] == 0:
            dfs(r,c)
            num += 1
cnt_list = collections.Counter(sum(sub_map,[]))

for r in range(N):
    for c in range(M):
        if MAP[r][c] == 1:
            temp = set()
            for i in range(4):
                nr, nc = r + NR[i], c + NC[i]
                if 0 <= nr < N and 0 <= nc < M:
                    if sub_map[nr][nc]:
                        temp.add(sub_map[nr][nc])
            result[r][c] += 1
            for i in temp:
                result[r][c] += cnt_list[i]
            result[r][c] %= 10

for i in range(N):
    print(''.join(map(str, result[i])))
