import sys, collections
N, M = map(int, sys.stdin.readline().split())
students = collections.defaultdict(list)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    students[a].append(b)

result = []
visit = [False] * N
def dfs(idx):
    visit[idx - 1] = True
    for s in students[idx]:
        if not visit[s - 1]:
            dfs(s)
    result.append(idx)

for s in range(1, N + 1):
    if not visit[s - 1]:
        dfs(s)

print(' '.join(map(str,result[::-1])))
