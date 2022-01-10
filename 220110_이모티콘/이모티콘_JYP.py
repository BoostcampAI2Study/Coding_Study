from collections import deque

n = int(input())
dp = [[-1] * 1001 for _ in range(1001)] # visited init
dp[1][0] = 0

q = deque()
q.append((1, 0))
ans = -1
while q:
    sc, cb = q.popleft()

    # rule1 => save to clipboard
    if dp[sc][sc] == -1:
        q.append((sc, sc))
        dp[sc][sc] = dp[sc][cb] + 1

    # rule2 => del screen -1
    if sc - 1 >= 0 and dp[sc - 1][cb] == -1:
        q.append((sc - 1, cb))
        dp[sc - 1][cb] = dp[sc][cb] + 1
        
    # rule3 => paste to screen
    if sc + cb <= n and dp[sc + cb][cb] == -1:
        q.append((sc + cb, cb))
        dp[sc + cb][cb] = dp[sc][cb] + 1


for i in range(n):
    if dp[n][i] != -1 and ans == -1 or ans > dp[n][i]:
        ans = dp[n][i]
print(ans)
