
def solution(N):
    # 예외 처리 변수
    exception = 0
    answer = 1
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'X':
                check3 = False
                for my, mx in adj:
                    ny, nx = i+my, j+mx
                    # 인접한 곳에 같은 색
                    if 0<=ny<N and 0<=nx<N and board[ny][nx] == 'X':
                        # 인접한 곳에 2개 있다면 3 리턴
                        if check3:
                            return 3
                        else:
                            answer = 2
                            check3 = True
                    else:
                        check3 = False
            else:
                exception += 1
    # X가 하나도 없으면 0 리턴
    if exception == N**2:
        return 0        
    return answer
    
N = int(input())
board = [input() for _ in range(N)]
# 인접 6개 + 1개
adj = [(0, -1), (-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1), (0, -1)]

print(solution(N))