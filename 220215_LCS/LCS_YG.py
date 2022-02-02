import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

LCS = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

for x in range(len(s1)+1):
    for y in range(len(s2)+1):

        if x == 0 or y == 0:
            continue

        # 문자가 같다면, 업데이트
        if s1[x-1] == s2[y-1]:
            LCS[x][y] = LCS[x-1][y-1]+1

        else:
            LCS[x][y] = max(LCS[x-1][y], LCS[x][y-1])


print(LCS[len(s1)][len(s2)])