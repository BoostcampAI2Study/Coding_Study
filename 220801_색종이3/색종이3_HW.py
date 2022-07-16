import sys
N = int(sys.stdin.readline())
LOCATIONS = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

paper = [[0] * 101 for _ in range(101)]
for r, c in LOCATIONS:
    for nr in range(r, r + 10):
        for nc in range(c, c + 10):
            paper[nr][nc] = 1

for r in range(1, 100):
    for c in range(1, 100):
        if paper[r][c] != 0:
            paper[r][c] += paper[r - 1][c]

result = 0
for r in range(1, 100):
    for w in range(1, 100):
        h = 100
        for k in range(w, 100):
            h = min(paper[r][k], h)
            if h == 0:
                break
            result = max(result, (k - w + 1) * h)

print(result)
