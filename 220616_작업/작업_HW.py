import sys, collections
N = int(sys.stdin.readline())
works, work_times, indegree = collections.defaultdict(list), [], []
q = collections.deque()
for idx in range(N):
    work_info = list(map(int, sys.stdin.readline().split()))
    work_times.append(work_info[0])
    indegree.append(work_info[1])
    if work_info[1] == 0:
        q.append(idx + 1)
    for w in range(work_info[1]):
        works[work_info[w + 2]].append(idx + 1)

dp = work_times[:]
while q:
    node = q.popleft()
    for w in works[node]:
        dp[w - 1] = max(dp[w - 1], dp[node - 1] + work_times[w - 1])
        indegree[w - 1] -= 1
        if indegree[w - 1] == 0:
            q.append(w)

result = 0
for i in range(N):
    result = max(result, dp[i])
print(result)
