from sys import stdin
from typing import List

def game(N:int, K:int, board_color:List, pieces:List, board:List):
    stack = 1
    count = 0
    direction = {
        0: (0, 1),
        1: (0, -1),
        2: (-1, 0),
        3: (1, 0)
    }
    # 반대방향
    reverse_dir = (1, 0, 3, 2)

    # 체스판 범위 밖인지
    def is_out_range(i:int, j:int):
        return not(-1 < i < N and -1 < j < N)
    
    # 다음 칸
    def next_location(i:int, j:int, dir:int):
        return i + direction[dir][0], j + direction[dir][1]

    # 움직일 칸이 흰색
    def white(order:int, i:int, j:int, ni:int, nj:int):
        move_pieces = board[i][j][order:]
        move(move_pieces, i, j, ni, nj)

        # 위치 정보 업데이트
        for k in move_pieces:
            i, j, order, dir = pieces[k]
            pieces[k] = (ni, nj, order+len(board[ni][nj]), dir)


    # 움직일 칸이 빨간색
    def red(order:int, i:int, j:int, ni:int, nj:int):        
        move_pieces = board[i][j][order:]
        move(move_pieces, i, j, ni, nj)
        
        # 순서 정보 및 위치 정보 업데이트
        for k in move_pieces:
            i, j, order, dir = pieces[k]
            pieces[k] = (ni, nj, K+1-order+len(board[ni][nj]), dir)


    # 움직일 칸이 파란색 혹은 체스판 범위 초과
    def blue(order:int, i:int, j:int, ni:int, nj:int):
        k = board[i][j][order]
        dir = pieces[k][3]
        pieces[k][3] = reverse_dir[dir]
        
        ni, nj = next_location(i, j, dir)

        # 체스판 벗어나는 경우 or 파란색인 경우
        if is_out_range(ni, nj) or board[ni][nj] == 2:
            return
        
        color[board_color[ni][nj]](order, i, j, ni, nj)
    

    # 체스판에서 말 움직임
    def move(move_pieces:List, i:int, j:int, ni:int, nj:int):
        # 보드에서 체스말 움직임
        board[ni][nj].extend(move_pieces)
        board[i][j] = board[i][j][:-(len(move_pieces)-1)]  

    
    color = {
        0: white,
        1: red,
        2: blue
    }
    

    while count < 1001:
        for k in range(K):
            i, j , order, dir = pieces[k]
            ni, nj = next_location(i, j, dir)

            if is_out_range(ni, nj):
                blue(order, i, j, ni, nj)
            else:
                color[board_color[ni][nj]](order, i, j, ni, nj)

        count += 1
        if stack > 3:
            return count

    return -1



if __name__ == '__main__':
    input = stdin.readline
    N, K = map(int, input().split())
    board_color = [list(map(int, input().split())) for n in range(N)]
    board = [[list() for n in range(N)] for n in range(N)]
    pieces = []
    for k in range(K):
        i, j, dir = map(int, input().split())
        i -= 1
        j -= 1
        pieces.append([i, j, dir-1, 0])
        board[i][j].append(k)

    print(game(N, K, board_color, pieces, board))