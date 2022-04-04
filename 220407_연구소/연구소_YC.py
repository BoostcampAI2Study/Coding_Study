from itertools import combinations
import copy
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

virus = [[row, col] for row in range(N) for col in range(M) if MAP[row][col] == 2]
no_walls = [[row, col] for row in range(N) for col in range(M) if MAP[row][col] == 0]

blocks = list(combinations(no_walls, 3))
answer = 0

for block in blocks:
    mmap = copy.deepcopy(MAP)
    for block_row, block_col in block:
        mmap[block_row][block_col] = 1

    queue = deque()
    for v in virus:
        queue.append(v)

    while queue:
        row,col = queue.popleft()

        for new_row, new_col in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
            if 0<=new_row<N and 0<=new_col<M and mmap[new_row][new_col] == 0:
                mmap[new_row][new_col] = 2
                queue.append([new_row, new_col])
        
    answer = max(answer, sum(map(lambda x: x.count(0), mmap)))

print(answer)
