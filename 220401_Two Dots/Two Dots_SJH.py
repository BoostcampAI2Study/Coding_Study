n, m = map(int, input().split())
board = [input() for _ in range(n)]

def dfs(nxt, visited, board, start, dots=1):
    i, j = nxt
    si, sj = start
    
    # 현재 지점 방문체크
    visited[i][j] = True
    color = board[si][sj]

    # 상하좌우 체크
    for _i, _j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni = i + _i
        nj = j + _j

        # 범위 벗어나지 않으면
        if -1 < ni < n and -1 < nj < m:
            if visited[ni][nj]:
                # 사이클 완성인가
                if ni == si and nj == sj and dots > 3:
                    print("Yes")
                    exit()

            # 완성되지 않았으면 다음 점으로 가기
            elif board[ni][nj] == color:
                dfs((ni, nj), visited, board, start, dots+1)



for i in range(n):
    for j in range(m):
        # 이미 사이클 체크한 경우 넘어가기
        visited = [[False]*m for _ in range(n)]
        dfs((i, j), visited, board, (i, j))


print("No")
