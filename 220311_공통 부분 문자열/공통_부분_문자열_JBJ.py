import sys

STRING_1 = sys.stdin.readline().strip()
STRING_2 = sys.stdin.readline().strip()

# index 0 is a margin. zero-padding
lcs_matrix = [[0]*(len(STRING_2)+1) for _ in range(len(STRING_1)+1)]
answer = 0
for str_1_idx in range(len(STRING_1)):
    for str_2_idx in range(len(STRING_2)):
        y, x = str_1_idx+1, str_2_idx+1
        #Longest Common Substring(AB, AAB) = Longest Common Substring(A, AA) + 1
        if STRING_1[str_1_idx] == STRING_2[str_2_idx]: 
            lcs_matrix[y][x] = lcs_matrix[y-1][x-1] + 1
            answer = max(answer, lcs_matrix[y][x])

print(answer)