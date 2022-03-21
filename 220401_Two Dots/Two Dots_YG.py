import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(x, y, cnt):
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < N and 0 <= ny < M and arr[x][y] == arr[nx][ny]:
            if (nx, ny) in visited:
                if cnt >= 4 and nx == tx and ny == ty:
                    print("Yes")
                    sys.exit()
            else:
                visited.add((nx, ny))
                dfs(nx, ny, cnt+1)


for x in range(N):
    for y in range(M):
        visited = set()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        tx, ty = x, y
        dfs(x, y, 1)

print("No")
