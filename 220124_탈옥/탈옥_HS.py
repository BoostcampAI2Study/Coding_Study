from itertools import combinations
from collections import deque

def escape(m, prisoner, doors_breaked):
    y, x = prisoner
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[0]*len(m[0]) for _ in range(len(m))]
    visited[y][x] = 1
    bfs = deque([(y, x)])
    while bfs:
        cy, cx = bfs.popleft()
        for my, mx in move:
            ny, nx = cy+my, cx+mx
            if 0 <= ny < len(m) and 0 <= nx < len(m[0]):
                if not visited[ny][nx]:
                    if m[ny][nx] in ['.', '$'] or (ny, nx) in doors_breaked:
                        bfs.append((ny, nx))
                        visited[ny][nx] = 1
            else:
                return True
    return False

C = int(input())
m = []
for _ in range(C):
    H, W = list(map(int, input().split()))
    doors, prisoners = [], []
    m = [input() for _ in range(H)]
    flag = False
    for y in range(H):
        for x in range(W):
            if m[y][x] == '#':
                doors.append((y, x))
            elif m[y][x] == '$':
                prisoners.append((y, x))
    if escape(m, prisoners[0], []) and escape(m, prisoners[1], []):
        print(0)
        continue
    for i in range(len(doors)):
        for door in combinations(doors, i):
            if escape(m, prisoners[0], door) and escape(m, prisoners[1], door):
                print(i)
                flag = True
                break
        if flag:
            break
    
