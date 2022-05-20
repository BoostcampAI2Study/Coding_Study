import collections

def bfs():
    N, K = map(int, input().split())
    k_locations, time = [K], 1
    while k_locations[-1] <= 500000:
        k_locations.append(k_locations[-1]+time)
        time += 1

    n_visited = {0:set([N]), 1:set()} # 0: visited points on even seconds, 1: visited points on odd seconds
    Q = collections.deque([(N, 0)])
    while Q:
        cur_n, move_time = Q.popleft()

        if move_time >= len(k_locations): continue
        if k_locations[move_time] in n_visited[move_time%2]: return move_time

        if 0 <= cur_n+1 <= 500000 and cur_n+1 not in n_visited[(move_time+1)%2]:
            n_visited[(move_time+1)%2].add(cur_n+1)
            Q.append((cur_n+1, move_time+1))
        if 0 <= cur_n-1 <= 500000 and cur_n-1 not in n_visited[(move_time+1)%2]:
            n_visited[(move_time+1)%2].add(cur_n-1)
            Q.append((cur_n-1, move_time+1))
        if 0 <= cur_n*2 <= 500000 and cur_n*2 not in n_visited[(move_time+1)%2]:
            n_visited[(move_time+1)%2].add(cur_n*2)
            Q.append((cur_n*2, move_time+1))
    return -1

print(bfs())