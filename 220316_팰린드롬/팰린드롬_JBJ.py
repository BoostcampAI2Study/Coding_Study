import sys

N = int(sys.stdin.readline().rstrip())
NUMS = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
QUESTIONS = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
palindromes = [[1 if i==j else 0 for j in range(N)] for i in range(N)]

"""
* 1 4 6
- * 2 5
- - * 3
- - - *
"""
for num_len in range(1, N):
    for start in range(N - num_len):
        end = start+num_len

        if NUMS[start] == NUMS[end]:
            if (end - start <= 1) or (end - start > 1 and palindromes[start+1][end-1]):
                palindromes[start][end] = 1

for start, end in QUESTIONS:
    print(palindromes[start-1][end-1])