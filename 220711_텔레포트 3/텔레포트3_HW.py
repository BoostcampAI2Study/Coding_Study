import sys, itertools
xs, ys = map(int, sys.stdin.readline().split())
xe, ye = map(int, sys.stdin.readline().split())
teleports = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

min_time = abs(xs - xe) + abs(ys - ye)
for sequence in itertools.permutations(range(3)):
    cur_x, cur_y = xs, ys
    dist = 10
    for teleport_idx in sequence:
        x1, y1, x2, y2 = teleports[teleport_idx]
        dist1, dist2 = abs(cur_x - x1) + abs(cur_y - y1), abs(cur_x - x2) + abs(cur_y - y2)
        if dist1 > dist2:
            cur_x, cur_y = x1, y1
            min_time = min(min_time, dist2 + abs(x1 - xe) + abs(y1 - ye) + dist)
            dist += (dist2 + 10)
        else:
            cur_x, cur_y = x2, y2
            min_time = min(min_time, dist1 + abs(x2 - xe) + abs(y2 - ye) + dist)
            dist += (dist1 + 10)
print(min_time)
