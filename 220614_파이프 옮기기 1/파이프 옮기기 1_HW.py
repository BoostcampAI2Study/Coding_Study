import sys
N = int(sys.stdin.readline())
HOUSE = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
move = 0
def dfs(r, c, d):
    global move
    if r == N - 1 and c == N - 1:
        move += 1
        return
      
    if r + 1 < N and c + 1 < N and not HOUSE[r + 1][c + 1] and not HOUSE[r + 1][c] and not HOUSE[r][c + 1]:
        dfs(r + 1, c + 1, 1)
    if d <= 1 and c + 1 < N and not HOUSE[r][c + 1]:
        dfs(r, c + 1, 0)
    if d >= 1 and r + 1 < N and not HOUSE[r + 1][c]:
        dfs(r + 1, c, 2)

dfs(0, 1, 0)
print(move)
