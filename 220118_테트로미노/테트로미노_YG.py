# 세로 크기 N, 가로 크기 M
N, M = map(int, input().split())

# 종이에 쓰여 있는 수 입력
paper = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우
dx = [0,1,0,-1]
dy = [1,0,-1,0]

max_value = max(map(max, paper))

answer = 0

visited = [[False]*M for _ in range(N)]

# dfs 함수 생성
def dfs(x, y, level, tetromino,value):
    global answer
    # 가능성없는 경우 pruning
    if answer >= value + (4-level)*max_value:
        return

    # 테트로미노완성시 값 업데이트
    if level == 4:
        answer = max(answer, value)
        return

    for tetro in tetromino:
        nx, ny = tetro
        for k in range(4):
            nnx, nny = nx+dx[k], ny+dy[k]
            if 0 <= nnx < N and 0 <= nny < M and visited[nnx][nny] == False:
                visited[nnx][nny] = True
                dfs(nnx, nny, level+1, tetromino+[(nnx, nny)],value+paper[nnx][nny])
                visited[nnx][nny] = False



# 좌표별로 search 진행
for x in range(N):
    for y in range(M):
        visited[x][y] = True
        dfs(x, y, 1, [(x,y)],paper[x][y])
        visited[x][y] = False


# 정답 출력
print(answer)