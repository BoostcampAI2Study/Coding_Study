import sys
sys.setrecursionlimit(10**9)

N, M = map(int, sys.stdin.readline().split())
MAZE = [sys.stdin.readline() for _ in range(N)]
dp = [[-1]*M for _ in range(N)] # -1: not visited, 0: cannot escape, 1: can escape
direction = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}

def dfs(y, x):
    global N, M, MAZE, dp, direction

    if not(0 <= y < N and 0 <= x < M): return 1 # out of range: escaping
    if dp[y][x] != -1: return dp[y][x] # visited (memoization)

    dp[y][x] = 0
    dp[y][x] = dfs(y+direction[MAZE[y][x]][0], x+direction[MAZE[y][x]][1])
    return dp[y][x]

escape_cnt = 0
for y in range(N):
    for x in range(M):
        if dp[y][x] == -1:
            if dfs(y, x) == 1: escape_cnt += 1
        elif dp[y][x] == 1:
            escape_cnt += 1

print(escape_cnt)