import sys, collections

N, K = map(int, sys.stdin.readline().strip().split())

def bfs(N, K):
    dp_times = [0] * int(1e5+1)
    Q = collections.deque()

    # location
    Q.append(N)
    
    while Q:
        location = Q.popleft()

        for move in (location+1, location-1, location*2):
            if 0 <= move <= 1e5 and not dp_times[move]:
                if move == K:
                    return dp_times[location]+1
                    
                dp_times[move] = dp_times[location]+1
                Q.append(move)

print(bfs(N, K) if N != K else 0)