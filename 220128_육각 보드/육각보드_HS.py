
import sys
# input = sys.stdin.readline

N = int(input())
board = [input() for _ in range(N)]
# 인접 6개
adj = [(0, -1), (-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1)]
# 색 채운 배열
fill = [[-1]*N for _ in range(N)]
# 색 리스트
color = [1]
# 예외 처리 변수
exception = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 'X':
            for c in color:
                for my, mx in adj:
                    ny, nx = i+my, j+mx
                    # 인접한 곳에 같은 색 있으면 break
                    if 0<=ny<N and 0<=nx<N and fill[ny][nx] == c:
                        break
                # 인접한 곳에 같은 색 없으면 색칠
                else:
                    fill[i][j] = c
                    break
            # 현재 색 리스트 안에서 색칠 못하면 하나 늘리기
            else:
                color.append(color[-1] + 1)
                fill[i][j] = color[-1]
        else:
            exception += 1

if exception == N**2:
    print(0)
else:
    print(color[-1])