import collections, sys

N, M, T = map(int, sys.stdin.readline().rstrip().split())
BOARD = [collections.deque(list(map(int, sys.stdin.readline().rstrip().split()))) for _ in range(N)]
ROTATES = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(T)]

for x, d, k in ROTATES:
    # rotation
    for idx in range(x-1, N, x):
        BOARD[idx].rotate(k if d == 0 else -k)

    # number check
    board_num_sum, isolated_set, delete_set = 0, set(), set()
    for y in range(N):
        for x in range(M):
            if BOARD[y][x]:
                isolation_flag = True
                board_num_sum += BOARD[y][x]
                for new_y, new_x in (y+1, x), (y-1, x), (y, x+1), (y, x-1):
                    new_x %= M # (M-1) - (1) - (2)
                    if 0 <= new_y < N and 0 <= new_x < M and BOARD[new_y][new_x]:
                        if BOARD[y][x] == BOARD[new_y][new_x]: # same numbers next to each other
                            isolation_flag = False
                            delete_set.add((y, x))
                            delete_set.add((new_y, new_x))
                if isolation_flag: # there are no same numbers around BOARD[y][x] 
                    isolated_set.add((y, x))
    if delete_set: # same number cases exist
        for dy, dx in delete_set:
            BOARD[dy][dx] = 0
    elif isolated_set: # same number cases do not exist
        average = board_num_sum / len(isolated_set)
        for y, x in isolated_set:
            if BOARD[y][x] > average:
                BOARD[y][x] -= 1
            elif BOARD[y][x] < average:
                BOARD[y][x] += 1

print(sum(map(sum, BOARD)))