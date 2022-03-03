from collections import deque

def func():
    global MAP, visited

    moves_r = [1,-1,0]
    moves_c = [1,-1,0]

    queue = deque()
    queue.append((7,0))

    while queue:
        cnt = len(queue)
        while cnt:
            row, col = queue.popleft()

            if (row, col) == (0,7):
                return 1

            if MAP[row][col] == '#':
                cnt-=1
                continue

            for mr in moves_r:
                for mc in moves_c:
                    new_row, new_col = row+mr, col+mc
                    if 0<=new_row<8 and 0<=new_col<8 and MAP[new_row][new_col] == '.':
                        if visited[new_row][new_col]<8:
                            visited[new_row][new_col] +=1
                            queue.append((new_row, new_col))
            cnt-=1        
        for i in range(7,0,-1):
            MAP[i] = MAP[i-1]
        MAP[0] = ['.']*8

    return 0

MAP = [list(input()) for _ in range(8)]
visited = [[0]*8 for _ in range(8)]

print(func())
