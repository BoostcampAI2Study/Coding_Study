import sys, collections
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())
stations = collections.defaultdict(list)
for _ in range(N):
    station1, station2 = map(int, sys.stdin.readline().split())
    stations[station1].append(station2)
    stations[station2].append(station1)

visit = [False] * (N + 1)
cycle_stations = []
def dfs(start, cur, n):
    if cycle_stations:
        return
    
    for station in stations[cur]:
        if not visit[station]:
            visit[station] = True
            dfs(start, station, n + 1)
            visit[station] = False
        else:
            if n >= 3 and station == start:
                for i in range(1, N + 1):
                    if visit[i]:
                        cycle_stations.append(i)
                cycle_stations.append(cur)
                return

for i in range(N):
    if not cycle_stations:
        visit[i+1] = True
        dfs(i+1,i+1, 1)
        visit[i+1] = False

answer = [0] * N
def bfs(station):
    visit = [False] * (N + 1)
    q = collections.deque()
    q.append((station, 0))
    visit[station] = True
    
    while q:
        node, move = q.popleft()
        if node in cycle_stations:
            answer[station - 1] = move
            return
        
        for next_station in stations[node]:
            if not visit[next_station]:
                q.append((next_station, move + 1))
                visit[next_station] = True

noncycle_stations = set(range(1, N+1)) - set(cycle_stations)
for station in noncycle_stations:
    bfs(station)

print(" ".join(map(str,answer)))
