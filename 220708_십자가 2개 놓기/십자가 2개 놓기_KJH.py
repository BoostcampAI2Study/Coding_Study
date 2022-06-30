# https://www.acmicpc.net/problem/17085
import sys


input = sys.stdin.readline

N, M = map(int, input().split())

board = [input().strip() for _ in range(N)]

candi = []


def find_leng(c_r, c_c):
    for i in range(min(N, M)):
        r, c = c_r, c_c
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + i * dr, c + i * dc
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == ".":
                    return i - 1
            else:
                return i - 1
    return i


def set_candi(c_r, c_c):
    leng = find_leng(c_r, c_c)
    for i in range(leng + 1):
        candi.append((c_r, c_c, i))


for r in range(N):
    for c in range(M):
        if board[r][c] == "#":
            set_candi(r, c)
answer = 0
for ar, ac, al in candi:
    for br, bc, bl in candi:
        if abs(ar - br) + abs(ac - bc) > min(al, bl) + min(
            max(abs(ar - br), abs(ac - bc)), max(al, bl)
        ):
            answer = max(answer, (al * 4 + 1) * (bl * 4 + 1))

print(answer)
