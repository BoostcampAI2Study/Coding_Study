N = int(input())
queens = [0]*N # queen locations(coordinates). queens[i] = j ==> (ith row, jth col) queen.
n_queen_cnts = 0

def is_valid(row_idx):
    global queens
    for prev_row_idx in range(row_idx): # because we put queens from top to bottom.
        if queens[row_idx] == queens[prev_row_idx]: return False # col check.
        if abs(row_idx - prev_row_idx) == abs(queens[row_idx] - queens[prev_row_idx]): return False # diagonal check.
    return True

def dfs(row_idx):
    global N, visited, n_queen_cnts

    if row_idx >= N:
        n_queen_cnts += 1
    else:
        for col_idx in range(N):
            queens[row_idx] = col_idx
            if is_valid(row_idx):
                dfs(row_idx+1)

dfs(0)
print(n_queen_cnts)