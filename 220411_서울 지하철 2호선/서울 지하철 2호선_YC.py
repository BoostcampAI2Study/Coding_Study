from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
big_circle = []

STATIONS=defaultdict(list)

for _ in range(N):
    start, end = map(int, input().split())
    STATIONS[start].append(end)
    STATIONS[end].append(start)

def dfs(circle, station):
    global big_circle

    for next_station in STATIONS[station]:
        if big_circle:
            return 
        if next_station in circle:
            if next_station != circle[-2]:
                big_circle = circle[circle.index(next_station):]
                return
            else:
                continue
        else:
            dfs(circle+[next_station], next_station)

dfs([N//2],N//2)
answer = [float('inf')] * (N+1)

queue = deque()

for c_station in big_circle:
    answer[c_station] = 0
    queue.append((c_station, 0))

while queue:
    s, dist = queue.popleft()
    for nxt_s in STATIONS[s]:
        if answer[nxt_s] == float('inf'):
            answer[nxt_s] = dist+1
            queue.append((nxt_s, dist+1))            

print(" ".join(map(str, answer[1:])))
