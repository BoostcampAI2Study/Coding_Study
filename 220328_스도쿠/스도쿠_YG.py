import sys
from collections import Counter
input = sys.stdin.readline

sdoku = [list(map(int, input().split())) for _ in range(9)]
blank = []

visited_horizon = [[False]*10 for _ in range(10)]
visited_vertical = [[False]*10 for _ in range(10)]
visited_3_x_3 = [[False]*10 for _ in range(10)]

for x in range(9):
    for y in range(9):
        if sdoku[x][y] == 0:
            blank.append((x, y))
        else:
            visited_horizon[x][sdoku[x][y]] = True
            visited_vertical[y][sdoku[x][y]] = True
            visited_3_x_3[3*(x//3)+y//3][sdoku[x][y]] = True

def dfs(level):
    if level == len(blank):
        for s in sdoku:
            print(" ".join(map(str, s)))
        sys.exit()

    x, y = blank[level]

    for value in range(1, 10):
        if visited_horizon[x][value] == False and visited_vertical[y][value] == False and visited_3_x_3[3*(x//3)+y//3][value] == False:
            visited_horizon[x][value], visited_vertical[y][value], visited_3_x_3[3*(x//3)+y//3][value] = True, True, True
            sdoku[x][y] = value
            dfs(level+1)
            sdoku[x][y] = 0
            visited_horizon[x][value], visited_vertical[y][value], visited_3_x_3[3*(x//3)+y//3][value] = False, False, False
dfs(0)