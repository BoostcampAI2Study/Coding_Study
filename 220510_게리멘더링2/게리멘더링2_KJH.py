import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
section_population = [0] * 5


def make_section(x, y, d1, d2):
    global N, section_population, board
    for r in range(N):
        dd1 = dd2 = r - x
        if r > x + d1:
            dd1 -= 2 * (r - (x + d1))
        if r > x + d2:
            dd2 -= 2 * (r - (x + d2))
        for c in range(N):
            if x <= r <= x + d1 + d2 and y - dd1 <= c <= y + dd2:
                section_population[4] += board[r][c]
            else:
                if 0 <= r < x + d1 and 0 <= c <= y:
                    section_population[0] += board[r][c]
                elif 0 <= r <= x + d2 and y < c < N:
                    section_population[1] += board[r][c]
                elif x + d1 <= r < N and 0 <= c < y + d2 - d1:
                    section_population[2] += board[r][c]
                elif x + d2 < r < N and y + d2 - d1 <= c < N:
                    section_population[3] += board[r][c]


answer = float("inf")
for x in range(N):
    for y in range(N):
        if x >= N - 2 or y == 0 or y == N - 1:
            continue
        for d2 in range(1, N - y):
            for d1 in range(1, min(y, N - d2 - x)):
                section_population = [0] * 5
                make_section(x, y, d1, d2)
                answer = min(answer, max(section_population) - min(section_population))


print(answer)
