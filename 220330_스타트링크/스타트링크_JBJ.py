import collections, sys

F, S, G, U, D = map(int, sys.stdin.readline().rstrip().split())

Q, visited = collections.deque([(S, 0)]), [True]+[False]*F
while Q:
    cur_floor, push_button_cnt = Q.popleft()

    if cur_floor == G:
        print(push_button_cnt)
        sys.exit()
    else:
        if cur_floor+U <= F and not visited[cur_floor+U]: # go up
            visited[cur_floor+U] = True
            Q.append([cur_floor+U, push_button_cnt+1])
        if cur_floor-D >= 1 and not visited[cur_floor-D]: # go down
            visited[cur_floor-D] = True
            Q.append([cur_floor-D, push_button_cnt+1])
print("use the stairs")
