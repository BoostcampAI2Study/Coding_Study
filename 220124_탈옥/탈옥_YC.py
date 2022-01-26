from collections import deque

def bfs(r, c, h, w, prison):
    move = [[1,0],[0,1],[-1,0],[0,-1]]
    visited = [[-1 for _ in range(w)] for _ in range(h)]

    answers = []

    queue = deque([[r, c, []]])

    while queue:
        row, col, door = queue.popleft()

        if row == 0 or col == 0 or row == h-1 or col == w-1:
            answers.append(door)

        for mr, mc in move:
            new_row, new_col = mr + row, mc + col
            if 0<=new_row<h and 0<=new_col<w:
                if prison[new_row][new_col] == '*':
                    continue
            
                if visited[new_row][new_col] == -1:
                    if prison[new_row][new_col] == '#':
                        door.append([new_row, new_col])
                    
                        visited[new_row][new_col] = len(door) 
                        queue.append([new_row, new_col, door])
                else:
                    if visited[new_row][new_col] > len(door):
                        if prison[new_row][new_col] == '#':
                            door.append([new_row, new_col])

                        visited[new_row][new_col] = len(door) 
                        queue.append([new_row, new_col, door]) 

testcase = int(input())

prison = []

for _ in range(testcase):
    h, w = map(int, input().split())

    for _ in range(h):
        prison.append(list(input()))
    
    for row in range(h):
        for col in range(w):
            if prison[row][col]=='$':
                a = bfs(row,col, h, w, prison)
                print(a)