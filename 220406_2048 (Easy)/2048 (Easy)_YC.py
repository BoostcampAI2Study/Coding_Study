from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
BOARD = [list(map(int, input().split())) for _ in range(N)]

def push(numbers):
    new_numbers = []
    idx = 0
    while idx < len(numbers):
        if idx < len(numbers)-1 and numbers[idx] == numbers[idx+1]:
            new_numbers.append(numbers[idx]*2)
            idx+=2
        else:
            new_numbers.append(numbers[idx])
            idx+=1
    new_numbers += [0] * (N-len(new_numbers))
    return new_numbers

def move(board, direction):
    new_board = [[]*N for _ in range(N)]

    if direction == 1:  # left
        for row in range(N):
            line = [board[row][col] for col in range(N) if board[row][col]]
            new_board[row] = push(line)
           
    elif direction == 2:    # right
        for row in range(N):
            line = [board[row][col] for col in range(N-1, -1, -1) if board[row][col]]
            new_board[row] = list(reversed(push(line)))
            
    elif direction == 3:    # up
        for col in range(N):
            line = [board[row][col] for row in range(N) if board[row][col]]
            new_line = push(line)
            for row in range(N):
                new_board[row].append(new_line[row])           

    else:
        for col in range(N):    # down
            line = [board[row][col] for row in range(N-1, -1, -1) if board[row][col]]
            new_line = list(reversed(push(line)))
            for row in range(N-1, -1, -1):
                new_board[row].append(new_line[row])

    return new_board

answer = 0
queue = deque()
queue.append((BOARD, 0))

while queue:
    board, depth = queue.popleft()

    if depth == 5:
        continue

    for direction in range(1, 5):   # 1 = left, 2 = right, 3 = up, 4 = down
        new_board = move(board, direction)
        queue.append((new_board, depth+1))
        answer = max(answer, max([max(row) for row in new_board]))

print(answer)
