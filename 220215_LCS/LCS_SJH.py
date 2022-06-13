seq1 = input()
seq2 = input()


# 마진 설정해주기
seq1 = ' ' + seq1
seq2 = ' ' + seq2

lcs = [[0] * len(seq2) for _ in range(len(seq1))]


for i in range(1, len(seq1)):
    for j in range(1, len(seq2)):
        if seq1[i] == seq2[j]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])


print(lcs[-1][-1])
