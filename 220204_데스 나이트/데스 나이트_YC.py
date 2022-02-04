from collections import deque

move=[[-2,-1],[-2,1],[0,-2],[0,2],[2,-1],[2,1]]

def bfs(r1,c1,r2,c2):
    answer=float('inf')
    visited = [[0 for _ in range(N)] for _ in range(N)]

    queue = deque([[r1, c1, 0]])

    while queue:
        r,c, moves = queue.popleft()

        if r == r2 and c == c2:
            if moves < answer: answer = moves
            
            continue
    
        for mr, mc in move:
            if 0 <= r+mr < N and 0 <= c+mc < N:
                if not visited[r+mr][c+mc] or moves+1 < visited[r+mr][c+mc]:
                    visited[r+mr][c+mc] = moves+1
                    queue.append([r+mr, c+mc, moves+1])

    return answer


N = int(input())

r1,c1,r2,c2 = map(int, input().split())

answer= bfs(r1,c1,r2,c2)

if answer == float('inf'): print(-1)
else: print(answer)
