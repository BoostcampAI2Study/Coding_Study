import sys, collections

T = int(sys.stdin.readline())

def bfs(start_y, start_x):
    global H, W, MAP, opened_doors
    min_opened_doors = [[-1] * (W+2) for _ in range(H+2)]

    Q = collections.deque()
    Q.append((start_y, start_x))
    min_opened_doors[start_y][start_x] = 0

    while Q:
        y, x = Q.popleft()
        # 0-1 bfs : append weight node(1) to the right, normal node(0) to the left
        for new_y, new_x in ((y, x+1), (y, x-1), (y+1, x), (y-1, x)):
            if 0 <= new_y < H+2 and 0 <= new_x < W+2:
                if min_opened_doors[new_y][new_x] == -1:
                    if MAP[new_y][new_x] == '#': # door (#) - weight node
                        min_opened_doors[new_y][new_x] = min_opened_doors[y][x] + 1
                        Q.append((new_y, new_x))
                    elif MAP[new_y][new_x] in ('.', '$'): # empty space (.) and prisoner ($) - normal node
                        min_opened_doors[new_y][new_x] = min_opened_doors[y][x]
                        Q.appendleft((new_y, new_x))
                    else: # wall (*) - skip
                        continue
    
    return min_opened_doors

for _ in range(T):
    H, W = map(int, sys.stdin.readline().strip().split())
    
    # enlarge the map to get sangkeun's bfs result
    MAP = ['.' * (W+2)]
    for _ in range(H):
        MAP.append('.' + sys.stdin.readline().strip() + '.')
    MAP.append('.' * (W+2))
    
    # get bfs results (sangkeun, prisoner_1, and prisoner_2)
    bfs_results = dict()
    bfs_results['sang_keun'] = bfs(0, 0)
    sang_keun = bfs(0, 0)
    num = 1
    for y in range(1, H+2):
        for x in range(1, W+2):
            if MAP[y][x] == '$' and num <= 2:
                bfs_results[f'prisoner_{num}'] = bfs(y, x)
                num+=1

    # get answer
    answer = sys.maxsize
    for y in range(1, H+2):
        for x in range(1, W+2):
            if bfs_results['sang_keun'][y][x] != -1 and bfs_results['prisoner_1'][y][x] != -1 and bfs_results['prisoner_2'][y][x] != -1:
                sum_results = bfs_results['sang_keun'][y][x] + bfs_results['prisoner_1'][y][x] + bfs_results['prisoner_2'][y][x]
                # de-duplication of opening the same door
                if MAP[y][x] == '#':
                    sum_results -= 2
                answer = min(answer, sum_results)

    print(answer)