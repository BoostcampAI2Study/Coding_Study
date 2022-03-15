import collections, itertools

N = int(input().rstrip())
SCVS = list(map(int, input().rstrip().split()))
while len(SCVS) < 3: SCVS.append(0)

# bfs (dp) - 136ms
DAMAGES = list(itertools.permutations([9, 3, 1], 3))
visited = [[[0]*61 for _ in range(61)] for _ in range(61)] # dp
Q = collections.deque([[0] + SCVS]) # attack_cnt, scvs
while Q:
    elements = Q.popleft()
    attack_cnt, scvs = elements[0], elements[1:]

    if sum(scvs) == 0:
        print(visited[0][0][0])
        break

    for damage in DAMAGES:
        scv_1, scv_2, scv_3 = [max(scvs[idx]-damage[idx], 0) for idx in range(3)]
        if not visited[scv_1][scv_2][scv_3]:
            visited[scv_1][scv_2][scv_3] = attack_cnt+1
            Q.append([attack_cnt+1, scv_1, scv_2, scv_3])

# dfs (dp) - 104ms
"""
def dfs(x, y, z):
    if x == 0 and y == 0 and z == 0:
        return 0
    if visited[x][y][z]:
        return visited[x][y][z]
    visited[x][y][z] = 1 + min(dfs(max(x-9, 0), max(y-3, 0), max(z-1, 0)), dfs(max(x-9, 0), max(y-1, 0), max(z-3, 0)), dfs(max(x-3, 0), max(y-9, 0), max(z-1, 0)),
                          dfs(max(x-3, 0), max(y-1, 0), max(z-9, 0)), dfs(max(x-1, 0), max(y-3, 0), max(z-9, 0)), dfs(max(x-1, 0), max(y-9, 0), max(z-3, 0)))
    return visited[x][y][z]

print(dfs(scv[0], scv[1], scv[2]))
"""