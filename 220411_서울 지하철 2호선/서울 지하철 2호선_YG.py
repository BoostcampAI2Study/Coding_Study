from collections import deque
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())

subway = [[] for _ in range(N+1)]

for _ in range(N):
    a, b = map(int, input().split())
    subway[a].append(b)
    subway[b].append(a)

visited_2 = [False] * (N + 1)

# 순환 체크
cycle = set()

def dfs(level, x, visited):
    global cycle
    if level < 3:
        for next_station in subway[x]:
            if visited_2[next_station] == False:
                visited_2[next_station] = True
                dfs(level+1, next_station, visited+[next_station])
                visited_2[next_station] = False
    else:
        for next_station in subway[x]:
            if visited_2[next_station] == False:
                visited_2[next_station] = True
                dfs(level+1, next_station, visited+[next_station])
                visited_2[next_station] = False
            else:
                if visited[0] == next_station:
                    for v in visited:
                        cycle.add(v)
                    return

for idx in range(1, N+1):
    if cycle:
        break
    visited_2[idx] = True
    dfs(1, idx, [idx])
    visited_2[idx] = False

answer = [1e9]*(N+1)
new_cycle = list(cycle)

# bfs를 통해 답 찾기
q = deque()

for c in new_cycle:
    answer[c] = 0
    q.append((c, 0))

while q:
    where, distance = q.popleft()

    for next_where in subway[where]:
        if answer[next_where] == 1e9:
            answer[next_where] = distance+1
            q.append((next_where, distance+1))

print(" ".join(map(str, answer[1:])))