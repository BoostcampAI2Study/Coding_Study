import sys

move = [(0, 1), (-1, 0), (-1,0), (1, 0)] # 오,왼,위,아래

input = sys.stdin.readline
N, K = map(int, input().split())
board_color = [list(map(int, input().split())) for n in range(N)]   # 체크판 색
board = [[list() for n in range(N)] for n in range(N)]  # 체스판 말 정보
pieces = [] # 체스말 정보

# # 1번 말부터 K번 말까지 정보 저장하면서 체스판에 놓기
# # 위치, 쌓인 순서, 이동 방향
for k in range(K):
    i, j , dir = map(int, input().split())
    i -= 1
    j -= 1
    dir -= 1
    board[i][j].append(k)
    pieces.append([i, j, dir, 0])

print(pieces)

# 1번 말부터 K번 말까지 순서대로 이동 진행
stack = 1
count = 0
while count < 1000:
    for k in range(K):
        i, j, dir, order = pieces[k]
        
        # 제일 아래 있는 경우에만 이동
        if order > 0:
            continue
        
        ni = i + move[dir][0]
        nj = j + move[dir][1]
            
        # 체스판 범위 벗어남 or 파란색
        # 이동 방향을 반대로 하고 한칸 이동. 바꾼 후 이동할 칸이 파란색이면 이동x
        if not -1 < ni < N or not -1 < nj < N or board_color[ni][nj] == 2:
            dir = (dir + 2) % 4
            pieces[k][2] = dir
            ni = i + move[dir][0]
            nj = j + move[dir][1]

            # 체스판 범위 벗어나면 이동하지 않음
            if not -1 < ni < N or not -1 < nj < N:
                continue
            
            # 다음 칸이 파란색이면 이동하지 않음
            if board_color[ni][nj] == 2:
                continue

        # 빨간색 1
        # 이동할 말의 쌓여있는 순서를 반대로 바꾼 후 가장 위에 올린다
        # 순서 반대로 바꾸기
        if board_color[ni][nj] == 1:
            board[i][j].reverse()       
            
            for k in range(K):
                pieces[k][3] = len(board[i][j]) - 1 - order

        # 공통
        # 가장 위에 올린다
        board[ni][nj] += board[i][j][:]
        board[i][j] = []

        for k in range(K):
            pieces[k][0] = ni
            pieces[k][1] = nj

        stack = max(stack, len(board[ni][nj]))
    
    count += 1
    if stack > 3:
        print(count)
        sys.exit()


print(-1)
