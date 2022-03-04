import collections, sys

boards = [input()[2:] for _ in range(3)] # (stick A, stick B, stick C)
BOARD_COUNTS = tuple(''.join(boards).count(circle_board) for circle_board in ('A', 'B', 'C'))
Q = collections.deque()
visited = set()

Q.append(boards + [0]) # (stick A, stick B, stick C, move count)
while Q:
    stick_A, stick_B, stick_C, move_cnt = Q.popleft()

    if (stick_A, stick_B, stick_C) in visited: continue
    visited.add((stick_A, stick_B, stick_C))

    if (stick_A.count('A'), stick_B.count('B'), stick_C.count('C')) == BOARD_COUNTS:
        print(move_cnt)
        break

    if stick_A:
        Q.append((stick_A[:-1], stick_B+stick_A[-1], stick_C, move_cnt+1)) # A -> B
        Q.append((stick_A[:-1], stick_B, stick_C+stick_A[-1], move_cnt+1)) # A -> C
    if stick_B:
        Q.append((stick_A+stick_B[-1], stick_B[:-1], stick_C, move_cnt+1)) # B -> A
        Q.append((stick_A, stick_B[:-1], stick_C+stick_B[-1], move_cnt+1)) # B -> C
    if stick_C:
        Q.append((stick_A+stick_C[-1], stick_B, stick_C[:-1], move_cnt+1)) # C -> A
        Q.append((stick_A, stick_B+stick_C[-1], stick_C[:-1], move_cnt+1)) # C -> B