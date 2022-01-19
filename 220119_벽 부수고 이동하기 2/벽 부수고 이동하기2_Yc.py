from collections import deque
import sys
input = sys.stdin.readline

move_x = [0,1,0,-1]
move_y = [1,0,-1,0]

N, M, K = map(int, input().split())

board = []
visited=[]

for _ in range(N):
    board.append(list(map(int,input().strip())))
    visited.append([False for _ in range(M)])

queue = deque([[0,0,1,K]])
visited[0][0]=True
answer=0

while queue:
    # 좌표, 깊이, 벽부수기 개수
    x,y,dp,br = queue.popleft()
    
    if x == N-1 and y == M-1:
        answer = dp
        break
    
    else:
        for mx, my in zip(move_x, move_y):
            nx, ny = x+mx, y+my
            
            if 0<=nx<N and 0<=ny<M: # 밖으로 나가지 않은 경우만
                if not visited[nx][ny]:
                    if board[nx][ny] == 1:
                        # 벽인데
                        if br > 0: #  뿌실수 있으면
                            queue.append([nx,ny,dp+1,br-1])
                        else:   # 못뿌시면
                            continue
                    else:
                        queue.append([nx,ny,dp+1,br])
        visited[x][y] = True
    

if answer:print(answer)
else: print(-1)




# import sys 
# input = sys.stdin.readline

# def dfs(x,y,bk,dp,arr):
#     if x == N-1 and y == M-1: 
#         arr.append(dp)
#         return
#     for mx, my in zip(move_x, move_y):
#         new_x = x + mx
#         new_y = y + my
#         if 0 <= new_x < N and 0 <= new_y < M:
#             if not visited[new_x][new_y]:
                
#                 if board[new_x][new_y] == 1:
#                     if bk > 0:
#                         visited[new_x][new_y] = True
#                         dfs(new_x, new_y,bk-1, dp+1, arr)
#                         visited[new_x][new_y] = False
#                     else: 
#                         continue

#                 else:
#                     visited[new_x][new_y] = True
#                     dfs(new_x, new_y, bk, dp+1, arr)
#                     visited[new_x][new_y] = False

# N, M, K = map(int, input().split())

# move_x = [1, 0, -1, 0]
# move_y = [0, 1, 0, -1]


# board = []
# visited = []
# for _ in range(N):
#     board.append(list(map(int, input().strip())))
#     visited.append([False for i in range(M)])

# visited[0][0]=True
# arr=[]

# dfs(0,0,K,1,arr)
# if arr:
#     print(min(arr))
# else:
#     print(-1)
