move = [(-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0)]

from collections import deque

N = int(input())
board = []
for _ in range(N):
    board.append(list(input()))

q=deque()
visited = [[0 for _ in range(N)] for _ in range(N)]

q.append((0,0))
            
Xs = []
for r, row in enumerate(board):
    for c, val in enumerate(row):
        if val == 'X':
            Xs.append((r, c))

def chk(r, c):
    tri = [
        [(0, -1), (-1, 0)], 
        [(-1, 0), (-1, 1)], 
        [(-1, 1), (0, 1)], 
        [(0, 1), (1, 0)], 
        [(1, 0), (1, -1)], 
        [(1, -1), (0, -1)]
    ]

    x = 0
    ans = 0
    for val in tri:
        
        dr1, dc1 = val[0]
        dr2, dc2 = val[1]
        r1, c1 = r + dr1, c + dc1
        r2, c2 = r + dr2, c + dc2

        if 0<=r1<N and 0<=c1<N and 0<=r2<N and 0<=c2<N:
            # print((r,c), (r1,c1), (r2,c2))
            x += 1
            if board[r1][c1] == 'X' and board[r2][c2] == 'X':
                return 3
            
            if board[r1][c1] == '-' and board[r2][c2] == '-':
                ans += 1
    if ans == x:
        return 1


cnt=0
if not Xs:
    print(0)
else:
    for r, c in Xs:
        if chk(r, c) == 3:
            print(3)
            exit()
        
        if chk(r, c) == 1:
            cnt += 1 
    
    if cnt == 0:
        print(2)
    else:
        print(1)

# print(visited)
# print(Xs)


