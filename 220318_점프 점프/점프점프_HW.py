import collections
N = int(input())
A = list(map(int, input().split()))
visit = [True] * N

result = 1e9
q = collections.deque()
q.append((0, 0))
while q:
    loc, jump_cnt = q.popleft()
    if loc == N - 1:
        if jump_cnt < result:
            result = jump_cnt
        continue
    for i in range(A[loc]):
        if loc + i + 1 < N and not visit[loc + i + 1]:
            q.append((loc + i + 1, jump_cnt + 1))
            visit[loc + i + 1] = True

print(result) if result != 1e9 else print(-1)
