import sys

move = {
            'right': (0, 1),
            'left': (0, -1),
            'up': (-1,0),
            'down': (1, 0)
    }

# 원래 방향 이름, 반대방향 인덱스
dir_info = [('right', 1), ('left', 0), ('up', 3), ('down', 2)]

input = sys.stdin.readline
N, K = map(int, input().split())
board_color = [list(map(int, input().split())) for n in range(N)]   # 체크판 색
board = [[list() for n in range(N)] for n in range(N)]  # 체스판 말 정보
pieces = [] # 체스말 정보

# # 1번 말부터 K번 말까지 정보 저장하면서 체스판에 놓기
# # 위치, 이동 방향
for k in range(K):
    i, j , dir = map(int, input().split())
    i -= 1
    j -= 1
    dir -= 1
    board[i][j].append(k)
    pieces.append([i, j, dir])


def blue_or_out(i, j):
    return not (-1 < ni < N and -1 < nj < N) or board_color[ni][nj] == 2



# 1번 말부터 K번 말까지 순서대로 이동 진행
stack = 1
count = 0
while count < 1001:
    for k in range(K):
        i, j, dir = pieces[k]
        
        # 제일 아래 있는 경우에만 이동
        if board[i][j][0] != k:
            continue
        
        _i, _j = move[dir_info[dir][0]]
        ni, nj = i + _i, j + _j
            
        # 체스판 범위 벗어남 or 파란색
        # 이동 방향을 반대로 하고 한칸 이동. 바꾼 후 이동할 칸이 파란색이면 이동x
        if blue_or_out(ni, nj):
            dir = dir_info[dir][1]
            pieces[k][2] = dir
            _i, _j = move[dir_info[dir][0]]
            ni = i + _i
            nj = j + _j

            # 다음 칸이 체스판 범위 벗어나거나 파란색이면 이동하지 않음
            if blue_or_out(ni, nj):
                continue

        # 빨간색 1
        # 이동할 말의 쌓여있는 순서를 반대로 바꾼 후 가장 위에 올린다
        # 순서 반대로 바꾸기
        if board_color[ni][nj] == 1:
            board[i][j].reverse()

        # 공통
        # 가장 위에 올린다
        board[ni][nj].extend(board[i][j])

        # 옮긴 말 정보 업데이트
        for k in board[i][j]:
            pieces[k][0] = ni
            pieces[k][1] = nj

        board[i][j] = []        

        # 최대로 쌓여있는 말 높이 업데이트
        stack = max(stack, len(board[ni][nj]))
    
    count += 1
    if stack > 3:
        print(count)
        sys.exit()


print(-1)
