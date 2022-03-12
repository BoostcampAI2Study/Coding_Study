import sys
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

target = list(map(int, input().split()))

if target[0] != 1:
    print(0)
    sys.exit()

expected = [0 for _ in range(N+1)]

for idx, value in enumerate(target):
    expected[value] = idx+1

for grp in graph:
    grp.sort(key=lambda x : expected[x])

answer = [0 for _ in range(N+1)]
cnt = 0
def dfs(value):
    global cnt
    cnt += 1
    answer[value] = cnt

    for next_v in graph[value]:
        if answer[next_v] != 0:
            continue
        dfs(next_v)
dfs(1)

print(int(answer == expected))