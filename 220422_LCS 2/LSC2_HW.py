import sys
sequences = [sys.stdin.readline().strip() for _ in range(2)]
len_seq1, len_seq2 = len(sequences[0]), len(sequences[1])
dp = [[0] * (len_seq2 + 1) for _ in range(len_seq1 + 1)]

for r in range(len_seq1):
    for c in range(len_seq2):
        if sequences[0][r] == sequences[1][c]:
            dp[r + 1][c + 1] = dp[r][c] + 1
        else:
            dp[r + 1][c + 1] = max(dp[r + 1][c], dp[r][c + 1])

r, c = len_seq1, len_seq2
subsequence = []
while len(subsequence) != dp[len_seq1][len_seq2]:
    if dp[r][c] == dp[r - 1][c]:
        r, c = r - 1, c
    elif dp[r][c] == dp[r][c - 1]:
        r, c = r, c - 1
    else:
        subsequence.append(sequences[0][r - 1])
        r, c = r - 1, c - 1

print(dp[len_seq1][len_seq2])
print(''.join(subsequence[::-1]))
