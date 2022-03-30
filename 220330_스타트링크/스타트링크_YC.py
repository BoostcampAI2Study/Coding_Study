from collections import deque
F, S, G, U, D = map(int, input().split())

answer = -1

visited = [False]*(F+1)
visited[S] = True

queue = deque()

if S == G:
    answer = 0
else:
    queue.append((S, 0))

while queue:
    floor, button_pressed = queue.popleft()

    for new_floor in [floor+U, floor-D]:
        if new_floor <= 0 or new_floor > F:
            continue

        if new_floor == G:
            answer = button_pressed+1
            break

        if not visited[new_floor]:
            visited[new_floor] = True
            queue.append((new_floor, button_pressed+1))

if answer!=-1:
    print(answer)
else:
    print("use the stairs")
