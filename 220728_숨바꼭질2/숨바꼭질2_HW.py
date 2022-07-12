import sys, collections

N, K = map(int, sys.stdin.readline().split())
dp = [1e9] * 100001

q = collections.deque()
q.append(N)
dp[N], cnt = 0, 0
while q:
    cur_loc = q.popleft()
    if cur_loc == K:
        cnt += 1
        continue
    for i in [-1, 1, cur_loc]:
        if 0 <= cur_loc + i <= 100000 and dp[cur_loc] + 1 <= dp[cur_loc + i]:
            q.append(cur_loc + i)
            dp[cur_loc + i] = dp[cur_loc] + 1

print(dp[K])
print(cnt)
