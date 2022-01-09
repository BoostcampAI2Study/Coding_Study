from collections import deque

# goal = 1000
goal = int(input())

visited=[]
for _ in range(1001):
    visited.append([False for _ in range(1001)])

queue = deque([[1,1,1]])

while queue:
    value,cpy,t = queue.popleft()
    
    if value == goal:
        break

    # delete
    if value - 1 != 0:
        new_v, new_cpy, new_t = value-1, cpy, t+1
        if not visited[new_v][new_cpy]:
            visited[new_v][new_cpy] = True
            queue.append([new_v, new_cpy, new_t])
    
    # ctrl +c
    new_v, new_cpy, new_t = value, value, t+1
    if not visited[new_v][new_cpy]:
        visited[new_v][new_cpy] = True
        queue.append([new_v, new_cpy, new_t])


    # ctrl+v
    if value + cpy < 1001:
        new_v, new_cpy, new_t = value + cpy, cpy, t+1
        if not visited[new_v][new_cpy]:
            visited[new_v][new_cpy] = True
            queue.append([new_v, new_cpy, new_t])

print(t)