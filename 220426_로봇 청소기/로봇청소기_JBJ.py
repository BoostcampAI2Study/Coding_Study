import collections, sys

while True:
    W, H = map(int, sys.stdin.readline().rstrip().split())
    if (W, H) == (0, 0): break
    ROOM = [[0]*W for _ in range(H)]
    visited = [[[False]*(1<<10) for _ in range(W)] for _ in range(H)]
    dirty_rooms_cnt, answer = 0, -1

    for y in range(H):
        rooms = sys.stdin.readline().rstrip()
        for x in range(W):
            if rooms[x] == '*':
                dirty_rooms_cnt += 1
                ROOM[y][x] = dirty_rooms_cnt # if there are 4 dirty rooms, all visited == 1111(2)
            elif rooms[x] == 'o':
                start_y, start_x = y, x
            elif rooms[x] == 'x':
                ROOM[y][x] = -1

    Q = collections.deque([(start_y, start_x, 0, 0)]) # robot coordinates, dirty rooms bitmasking, move_cnt 
    while Q:
        y, x, dirty_bits, move_cnt = Q.popleft()

        if dirty_bits == (1<<dirty_rooms_cnt)-1:
            answer = move_cnt
            break
        else:
            for new_y, new_x in (y+1, x), (y-1, x), (y, x+1), (y, x-1):
                if 0 <= new_y < H and 0 <= new_x < W and ROOM[new_y][new_x] != -1:
                    # if ROOM[new_y][new_x] > 0, currently in the dirty room, e.g. visiting 3rd dirty room, 011(2) -> 111(2)
                    new_dirty_bits = dirty_bits | (1<<(ROOM[new_y][new_x]-1)) if ROOM[new_y][new_x] > 0 else dirty_bits
                    if not visited[new_y][new_x][new_dirty_bits]:
                        Q.append((new_y, new_x, new_dirty_bits, move_cnt+1))
                        visited[new_y][new_x][new_dirty_bits] = True
    print(answer)
