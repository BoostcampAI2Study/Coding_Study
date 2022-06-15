import sys

N, M = map(int, sys.stdin.readline().split())
BOARD = [sys.stdin.readline().rstrip() for _ in range(N)]
STARS, CROSSES = set(), set()
for n in range(N):
    for m in range(M):
        if BOARD[n][m] == '*': STARS.add((n , m))

for n in range(N):
    for m in range(M):
        if BOARD[n][m] == '*':
            size = 0
            for d in range(1, M if N > M else N):
                if 0 <= n-d <= n+d < N and 0 <= m-d <= m+d < M and BOARD[n-d][m] == BOARD[n+d][m] == BOARD[n][m-d] == BOARD[n][m+d] == '*':
                    size = d
                    STARS -= set([(n-d, m), (n+d, m), (n, m-d), (n, m+d), (n, m)])
                else:
                    break
            if size: CROSSES.add((n+1, m+1, size))
            
if STARS:
    print(-1)
else:
    print(len(CROSSES))
    for n, m, d in CROSSES:
        print(n, m, d)