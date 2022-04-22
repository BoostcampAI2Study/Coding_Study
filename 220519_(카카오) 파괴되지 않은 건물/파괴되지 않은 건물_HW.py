# ref: https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/
def solution(board, skill):
    answer = 0
    prefix_sum = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for t, r1, c1, r2, c2, degree in skill:
        prefix_sum[r1][c1] += degree if t == 2 else -degree
        prefix_sum[r1][c2 + 1] += degree if t == 1 else -degree
        prefix_sum[r2 + 1][c1] += degree if t == 1 else -degree
        prefix_sum[r2 + 1][c2 + 1] += degree if t == 2 else -degree
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            prefix_sum[r][c + 1] += prefix_sum[r][c]
            
    for c in range(len(board[0])):
        for r in range(len(board)):
            prefix_sum[r + 1][c] += prefix_sum[r][c]
            if board[r][c] + prefix_sum[r][c] >= 1:
                answer += 1
    return answer

# 내가 작성한 코드
# 정확성: 53.8
# 효율성: 0.0
# 합계: 53.8 / 100.0
def solution(board, skill):
    answer = 0
    for t, r1, c1, r2, c2, degree in skill:
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                board[r][c] += degree if t == 2 else -degree
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] >= 1:
                answer += 1
    return answer
