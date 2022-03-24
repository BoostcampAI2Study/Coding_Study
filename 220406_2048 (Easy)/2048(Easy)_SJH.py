from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


if n == 1:
    print(board[0][0])

else:
    # 시계 방향으로 돌리기
    def rotate(board):
        return [[board[n-j-1][i] for j in range(n)] for i in range(n)]

    # 반시계 방향으로 돌리기
    def rotate_opposite(board):        return [[board[j][n-i-1] for j in range(n)] for i in range(n)]
        
    # 왼쪽으로 밀기
    def left(board):
        new_board = []

        for row in board:
            # 열 값이 모두 0이면
            if set(row) == {0}:
                new_board.append(row)
                continue
            
            new_row = [0] * n    # 왼쪽으로 민 열
            prev = 0

            for nxt in range(n):
                # 둘이 같은 숫자 (0 아님)
                if new_row[prev] == row[nxt] != 0:
                    new_row[prev] *= 2
                    prev += 1
                else:
                    # 아직 숫자블록을 본 적 없으면
                    if new_row[prev] == 0:
                        new_row[prev] = row[nxt]
                    # 다음 블록이 0이면
                    elif row[nxt] == 0:
                        continue                    
                    # 이전 블록이 숫자 블록이었으면 다음 자리에 쌓기
                    else:
                        prev += 1
                        new_row[prev] = row[nxt]


            # 왼쪽으로 민 열 보드에 추가
            new_board.append(new_row)

        return new_board


    def up(board):
        # 보드 반시계 방향으로 한번 돌리기
        new_board = rotate_opposite(board)
        
        # 왼쪽으로 밀기
        new_board = left(new_board)
        
        # 보드 다시 원래대로 돌리기 (시계방향 한번)
        new_board = rotate(new_board)

        return new_board


    def down(board):
        # 보드 시계 방향으로 한번 돌리기
        new_board = rotate(board)

        # 왼쪽으로 밀기
        new_board = left(new_board)

        # 보드 다시 원래대로 돌리기 (반시계방향 한번)
        new_board = rotate_opposite(new_board)

        return new_board


    def right(board):
        # 보드 반시계 방향으로 두번 돌리기
        new_board = board
        for _ in range(2):
            new_board = rotate_opposite(new_board)

        # 왼쪽으로 밀기
        new_board = left(new_board)

        # 보드 다시 원래대로 돌리기 (시계방향 두번)
        for _ in range(2):
            new_board = rotate(new_board)

        return new_board


    direction = {'u': up, 'd': down, 'l': left, 'r': right}

    answer = 0
    queue = deque([(0, board)])

    # bfs로 탐색
    while queue:
        count, board = queue.popleft()

        if count < 5:
            count += 1

            for d in direction:
                new_board = direction[d](board)

                for row in new_board:
                    answer = max(answer, max(row))

                queue.append((count, new_board))

    print(answer)