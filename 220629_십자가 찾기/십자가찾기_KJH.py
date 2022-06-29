# https://www.acmicpc.net/problem/16924

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
answer = []


def find_leng(c_r, c_c):
    add_answer = set()
    for i in range(min(N, M)):
        r, c = c_r, c_c
        stack = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + i * dr, c + i * dc
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == ".":
                    for tmp_r, tmp_c in stack:
                        add_answer.discard((tmp_r, tmp_c))
                    return i - 1, add_answer
                if not visited[nr][nc]:
                    add_answer.add((nr, nc))
                stack.append((nr, nc))
            else:
                for tmp_r, tmp_c in stack:
                    add_answer.discard((tmp_r, tmp_c))
                return i - 1, add_answer
    return i, add_answer


def set_visited(c_r, c_c):
    leng, new_visit = find_leng(c_r, c_c)
    if leng > 0:
        for dr, dc in new_visit:
            visited[dr][dc] = 1
        if new_visit:
            answer.append(f"{c_r+1} {c_c+1} {leng}")


for r in range(N):
    for c in range(M):
        set_visited(r, c)
for r in range(N):
    for c in range(M):
        if board[r][c] == "*" and not visited[r][c]:
            print(-1)
            sys.exit()

print(len(answer))
for an in answer:
    print(an)
