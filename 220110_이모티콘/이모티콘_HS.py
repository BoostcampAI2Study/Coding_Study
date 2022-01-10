from collections import deque, defaultdict
s = int(input())

# 복사하는데 1초
# 붙여넣는데 1초
# 제거하는데 1초
answer = 0

d = defaultdict(int)
d[1] = 0
bfs = deque([[1, 0, 0, True]])  # the number of screen, clip, time, copy
while bfs:
    screen, clip, time, copy = bfs[0]
    if screen == s:
        print(time)
        break
    if screen > s:
        print(time + screen - s)
        break
    # copy
    if copy:
        bfs.append([screen, screen, time+1, False])
    # paste
    if clip > 0:
        if d[screen+clip] == 0 or d[screen+clip] > time+1:
            bfs.append([screen+clip, clip, time+1, True])
    # eliminate
    if screen > 1:
        if d[screen-1] == 0 or d[screen-1] > time +1:
            bfs.append([screen-1, clip, time+1, True])
    bfs.popleft()