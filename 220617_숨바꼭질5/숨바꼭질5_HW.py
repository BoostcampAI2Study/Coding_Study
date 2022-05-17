import sys, collections
N, K = map(int, sys.stdin.readline().split())
def bfs():
    q = collections.deque()
    q.append((N, 0))
    visit = [[False] * int(5e5 + 1) for _ in range(2)]
    visit[0][N] = True

    while q:
        n, time = q.popleft()
        nk = K + time * (time + 1) // 2
        if nk <= 5e5:
            if visit[time % 2][nk]:
                return time

            for nn in [n - 1, n + 1, n * 2]:
                if 0 <= nn <= 5e5 and not visit[(time + 1) % 2][nn]:
                    q.append((nn, time + 1))
                    visit[(time + 1) % 2][nn] = True
    return -1
print(bfs())
