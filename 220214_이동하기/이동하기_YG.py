import sys

input = sys.stdin.readline

N, M = map(int, input().split())

MIRO = [list(map(int, input().split())) for _ in range(N)]

for x in range(N):
    for y in range(M):
        if x == 0 and y == 0:
            continue
        elif x == 0 and y != 0:
            MIRO[x][y] += MIRO[x][y-1]
        elif x != 0 and y == 0:
            MIRO[x][y] += MIRO[x-1][y]
        else:
            MIRO[x][y] += max(MIRO[x-1][y], MIRO[x][y-1])

print(MIRO[N-1][M-1])