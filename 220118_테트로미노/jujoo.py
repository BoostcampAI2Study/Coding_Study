# 종이에 쓰인 숫자가 무엇?
# 첫째줄이 최대가 되야되는데 첫째줄이 위에서 첫째? 밑에서 첫째?
class tetris:
    def __init__(self, mat):
        self.mat = mat
        shape = {0: []}
if __name__ == '__main__':
    N, M = 5, 5
    mat = [[1, 2, 3, 4 ,5], [5, 4, 3, 2, 1], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [1, 2, 1, 2, 1]]

# -- 정답
import sys; input = sys.stdin.readline

def dfs(r, c, idx, total):
    global ans
    # -- pruning
    if ans >= total + max_val * (3 - idx):
        return
        
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if idx == 1: # ㅜ 모양
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visit[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr))

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)
