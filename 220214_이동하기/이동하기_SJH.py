from sys import stdin

input = stdin.readline
N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

candies = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        candies[i][j] = maze[i-1][j-1] + max(candies[i-1][j], candies[i][j-1], candies[i-1][j-1])

print(candies[-1][-1])