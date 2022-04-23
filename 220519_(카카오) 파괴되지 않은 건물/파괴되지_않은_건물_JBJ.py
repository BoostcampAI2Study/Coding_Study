def solution(board, skill):
    undestroyed_buildings, Y, X = 0, len(board), len(board[0])
    delta = [[0]*(X+1) for _ in range(Y+1)] # cumulative sum list
    
    for type_, y1, x1, y2, x2, degree in skill:
        degree = degree if type_ == 2 else (-degree)
        # get cumulative sums.   
        delta[y1][x1] += degree
        delta[y1][x2+1] -= degree
        delta[y2+1][x1] -= degree
        delta[y2+1][x2+1] += degree
    
    for y in range(Y+1): # row-wise cumulative sum operations.
        for x in range(X):
            delta[y][x+1] += delta[y][x]
    
    for x in range(X+1): # column-wise cumulative sum operations.
        for y in range(Y):
            delta[y+1][x] += delta[y][x]    
    
    for y in range(Y): # count undestroyed buildings.
        for x in range(X):
            if board[y][x] + delta[y][x] > 0:
                undestroyed_buildings += 1
    
    return undestroyed_buildings