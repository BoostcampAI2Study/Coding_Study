import sys, collections

F, S, G, U, D = map(int, sys.stdin.readline().split())
def bfs():
    visited = [False] * (F + 1)
    q = collections.deque()
    q.append((S, 0))
    visited[S] = True

    while q:
        cur_floor, move = q.popleft()
        if cur_floor == G:
            print(move)
            return
        if cur_floor + U <= F and not visited[cur_floor + U]:
            visited[cur_floor + U] = True
            q.append((cur_floor + U, move + 1))
        if cur_floor - D > 0 and not visited[cur_floor - D]:
            visited[cur_floor - D] = True
            q.append((cur_floor - D, move + 1))
    print("use the stairs")
bfs()
